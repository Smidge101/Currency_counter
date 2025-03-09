from django.http import HttpResponse, JsonResponse
import requests 
from . import Constants
from . import manual
import sqlite3
from django.views import View
from django.utils.decorators import async_only_middleware

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

    return HttpResponse(res.fetchone())

def getExchangeRates(request):
    service_key = Constants.API_KEY_SERVICE
    #  Making request
    url = f"https://v6.exchangerate-api.com/v6/{service_key}/latest/USD"

    #  making request
    try:
        response = requests.get(url)
        data = response.json()
        rates = data.get("conversion_rates", {})
        return JsonResponse(rates)
    except request.exceptions.RequestException as e:
        return JsonResponse({"error": "Failed to fetch data", "details": str(e)})
    
    