from django.http import HttpResponse, JsonResponse
import requests 
from . import Constants
from . import manual
import sqlite3
import json
from django.views import View
from django.utils.decorators import async_only_middleware

from rest_framework.decorators import api_view
from rest_framework.response import Response

# def home(request):
#     conn = manual.get_db_connection() 
#     cursor = conn.cursor() 
#     res = cursor.execute("""CREATE TABLE IF NOT EXISTS currency 
#                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                          name TEXT NOT NULL, 
#                          rate DOUBLE NOT NULL);""")
#     print(res.fetchone()) 
#     conn.commit() 
#     conn.close()

#     return HttpResponse(res.fetchone())

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
    
@api_view(['POST'])
def convert_currency(request):
    usd = request.data.get('usd')
    selection = request.data.get('selection')
    
    if not usd or not selection:
        return Response({"error": "Missing required fields."}, status=400)
    rate = 1.28
    
    converted_amount = usd * rate
    return Response({"converted_amount": converted_amount}, status=200)
    
    
    # todo get database
    