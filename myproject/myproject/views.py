from django.http import HttpResponse, JsonResponse
import requests 
import Constants

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

