"""Kenyan Business Currency Tracker
-------------------
Command tool that takes KES and converts to USD, EUR, and GBP using live exchange rate API.

Usage:
    python day5_week1_project.py

Requirements:
    pip install requests python-dotenv
"""
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("EXCHANGERATE_API_KEY")

def convert_currency(amount, from_currency, to_currency):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # raises HTTPError for bad responses
        data = response.json()
        rates = data.get("rates", {})
        if to_currency in rates:
            return amount * rates[to_currency]
        else:
            print(f"Currency {to_currency} not available in API response.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rate: {e}")
        return None
    except (ValueError, KeyError) as e:
        print(f"Error processing data: {e}")
        return None

def run_tool():
    print("Kenyan Business Currency Tracker")
    print("-------------------")

    try:
        amount_str = input("Enter amount in KES: ").strip()
        if not amount_str:
            print("Please enter amount.")
            return

        amount = float(amount_str)
    except ValueError:
        print("Invalid input. Please enter a numeric amount.")
        return

    print(f"\n=== Exchange Rates for {amount} KES ===")
    for currency in ["USD", "EUR", "GBP"]:
        converted_amount = convert_currency(amount, "KES", currency)
        if converted_amount is not None:
            print(f"{currency}: {converted_amount:.2f}")
        else:
            print(f"Could not convert to {currency}.")

if __name__ == "__main__":
    run_tool()
