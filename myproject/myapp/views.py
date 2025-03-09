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
    service_key = Constants.API_KEY_SERVICE
    #  Making request
    url = f"https://v6.exchangerate-api.com/v6/{service_key}/latest/USD"

    #  making request
    try:
        response = requests.get(url)
        data = response.json()
        logger.debug()
        rates = data.get("conversion_rates", {})
        

        for currency_code, exchange_rate in rates.items():
            Currency.objects.get_or_create(

                code = currency_code,

                defaults={'name': currency_code, 'exchange_rate': exchange_rate}
            )
       # return HttpResponse("Data successfully inserted into the database!")
        return JsonResponse(rates, safe=False) 
    except request.exceptions.RequestException as e:
        return JsonResponse({"error": "Failed to fetch data", "details": str(e)})
    
