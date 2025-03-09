from django.http import HttpResponse, JsonResponse
import requests 
import json 
import logging
from myapp import Constants
from . import manual
import sqlite3
from django.views import View
from django.utils.decorators import async_only_middleware
from .models import Currency

logger = logging.getLogger(__name__)

def home(request):
    conn = manual.get_db_connection() 
    cursor = conn.cursor() 
    res = cursor.execute("""CREATE TABLE IF NOT EXISTS currency 
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         name TEXT NOT NULL, 
                         rate DOUBLE NOT NULL);""")
    print(res.fetchone()) 
    conn.commit() 
    conn.close()

    return None

def getExchangeRates(request):
    service_key = Constants.API_KEY_SERVICE  # Your API key from settings
    url = f"https://v6.exchangerate-api.com/v6/{service_key}/latest/USD"

    try:
        # Make the HTTP request to the API
        response = requests.get(url)
        response.raise_for_status()  # This will raise an error for any bad HTTP status

        data = response.json()
        rates = data.get("conversion_rates", {})

        # Insert each exchange rate into the database using Django ORM
        for currency_code, exchange_rate in rates.items():
            Currency.objects.get_or_create(
                name=currency_code,  # Use 'name' instead of 'code'
                defaults={'name': currency_code, 'rate': exchange_rate}
            )

        # Return the exchange rates as a JSON response
        return JsonResponse(rates, safe=False)

    except requests.exceptions.RequestException as e:  # Fix: Use 'requests' instead of 'request'
        # Handle request exceptions like network issues or bad status codes
        logger.error(f"Error fetching exchange rates: {e}")
        return JsonResponse({"error": "Failed to fetch data", "details": str(e)})