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
from rest_framework import status
from .models import Currency

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

def populate_currency_data():
    service_key = Constants.API_KEY_SERVICE
    #  Making request
    url = f"https://v6.exchangerate-api.com/v6/{service_key}/latest/USD"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
        rates = data.get("conversion_rates", {})

        for currency_name, rate in rates.items():
            # Update if exists, otherwise create a new one
            Currency.objects.update_or_create(
                name=currency_name,
                defaults={"rates": rate}
            )
        print("Currency data updated successfully!")
    else:
        print(f"Failed to fetch data. Status Code: {response.status_code}")


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
    
    print(f"Received USD: {usd}, Selection: {selection}")
    if not usd or not selection:
        return Response({"error": "Missing required fields."}, status=400)
    
    try:
        currency = Currency.objects.get(name=selection)
        rate = currency.rates
    except Currency.DoesNotExist as e:
        print(f"Error: {str(e)}")
        return Response({"error": f"Invalid currency selection.'{selection}'"}, status=status.HTTP_400_BAD_REQUEST)
    
    converted_amount = float(usd) * rate
    return Response({"converted_amount": converted_amount}, status=200)
