from django.http import HttpResponse, JsonResponse
import requests 
import Constants
import aiohttp
from django.views import View
from django.utils.decorators import async_only_middleware

def home(request):
    return HttpResponse("Hello World hehe")

def getExchangeRates(request):
    service_key = Constants.API_KEY_SERVICE
#Making request
    url = f"https://v6.exchangerate-api.com/v6/{service_key}/latest/USD"

    #making request
    try:
        response = requests.get(url)
        data = response.json()
        return JsonResponse(data, safe=False)
    except request.exceptions.RequestException as e:
        return JsonResponse({"error": "Failed to fetch data", "details": str(e)})
    
class CurrencyRateView(View):
    async def get(self, request):
        service_key = Constants.API_KEY_SERVICE
    #Making request
        url = f"https://v6.exchangerate-api.com/v6/{service_key}/latest/USD"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.json()
                    rates = data.get("conversion_rates", {})
                    return JsonResponse(rates)
        except aiohttp.ClientError as e:
            return JsonResponse({"error": str(e)}, status = 500)