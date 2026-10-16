import requests
import os
from dotenv import load_dotenv

load_dotenv()
from requests.auth import HTTPBasicAuth

consumer_key = os.environ["SAFARICOM_CONSUMER_KEY"]
consumer_secret = os.environ["SAFARICOM_CONSUMER_SECRET"]
api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

response = requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
access_token = response.json()["access_token"]
print("Access Token:", access_token)

