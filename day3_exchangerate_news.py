"""Exchange Rate News Tool
-------------------
Shows Exchange Rate news and current exchange rates.

Usage:
    python day3_exchangerate_news.py

Requirements:
    pip install requests python-dotenv
"""
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("NEWSAPI_KEY")

def get_news(country):
    # Search specifically for exchange rate–related news mentioning the country
    query = f"{country} exchange rate"
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def get_exchange_rate(base_currency="USD"):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def run_tool():
    print("Exchange Rate News Tool")
    print("-------------------")
    country = input("Enter a country name: ").strip()

    if not country:
        print("No country entered. Exiting.")
        return

    print(f"\nFetching exchange rate news for {country}...")

    news_data = get_news(country)
    exchange_data = get_exchange_rate("USD")

    # Show news
    if not news_data or not news_data.get("articles"):
        print(f"Could not find exchange rate news for '{country}'.")
    else:
        print(f"\n=== Exchange Rate News Articles ===")
        for article in news_data["articles"]:
            title = article.get("title", "No title")
            source = article.get("source", {}).get("name", "Unknown source")
            published = article.get("publishedAt", "Unknown date")
            print(f"- {title} ({source}, {published})")

    # Show exchange rates
    if not exchange_data or not exchange_data.get("rates"):
        print("\nCould not fetch exchange rate data.")
    else:
        print(f"\n=== Exchange Rates (Base: {exchange_data.get('base', 'USD')}) ===")
        for currency, rate in exchange_data["rates"].items():
            print(f"{currency}: {rate}")

if __name__ == "__main__":
    run_tool()

