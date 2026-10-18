"""Run with the virtual environment's Python, then visit localhost:8000."""

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, quote, urlparse

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")


class CountryHandler(BaseHTTPRequestHandler):
    def send_body(self, status, body, content_type):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def send_json(self, status, payload):
        self.send_body(status, json.dumps(payload).encode(), "application/json; charset=utf-8")

    def do_GET(self):
        url = urlparse(self.path)
        if url.path in ("/", "/day4_fetch.html"):
            self.send_body(200, (ROOT / "day4_fetch.html").read_bytes(), "text/html; charset=utf-8")
            return
        if url.path != "/api/country":
            self.send_json(404, {"error": "Not found"})
            return
        country = parse_qs(url.query).get("name", [""])[0].strip()
        if not country:
            self.send_json(400, {"error": "Please enter a country name."})
            return
        key = os.getenv("RESTCOUNTRIES_API_KEY")
        if not key:
            self.send_json(503, {"error": "Set RESTCOUNTRIES_API_KEY in your .env file and restart the server."})
            return
        try:
            response = requests.get(
                "https://api.restcountries.com/countries/v5/names.common/" + quote(country, safe=""),
                headers={"Authorization": f"Bearer {key}"}, timeout=15,
            )
            if not response.ok:
                message = "Check your REST Countries key and account permissions." if response.status_code in (401, 403) else "Country lookup failed. Check the name and try again."
                self.send_json(response.status_code, {"error": message})
                return
            self.send_json(200, response.json())
        except (requests.RequestException, ValueError):
            self.send_json(502, {"error": "Unable to contact REST Countries. Please try again."})


if __name__ == "__main__":
    print("Country Info: http://localhost:8000 (Ctrl+C to stop)", flush=True)
    ThreadingHTTPServer(("127.0.0.1", 8000), CountryHandler).serve_forever()
