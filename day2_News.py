import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("NEWSAPI_KEY")
country = 'Uganda'
url = f"https://newsapi.org/v2/everything?q={country}&apiKey={api_key}"
response = requests.get(url)
if response.status_code == 200:
     data = response.json()
     articles = data['articles']
     for article in articles:
         title = article['title']
         description = article['description']
         url = article['url']
         print(f"Title: {title}")
         print(f"Description: {description}")
         print(f"URL: {url}")
         print()
elif response.status_code == 404:
     print(f"Country not found: {country}. Check spelling.")
elif response.status_code == 401:
     print("API key is invalid or missing.Check your .env file")
elif response.status_code == 429:
     print("Too many requests. Wait before making another request")
else:
     print(f"Unexpected error: {response.status_code}")
     print(response.text)