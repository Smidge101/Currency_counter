from django.core.management.base import BaseCommand
import requests
from myapp.models import Currency
from myapp import Constants
import logging

# Initialize logger
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Fetches exchange rates from the API and updates the conversion rates in the database'

    def handle(self, *args, **kwargs):
        service_key = Constants.API_KEY_SERVICE
        url = f"https://v6.exchangerate-api.com/v6/{service_key}/latest/USD"

        # Make the API request
        try:
            response = requests.get(url)
            data = response.json()

            # Check if the response is valid
            if response.status_code != 200 or "conversion_rates" not in data:
                self.stdout.write(self.style.ERROR("Error fetching data from the API"))
                return

            rates = data["conversion_rates"]

            # Update the database with the exchange rates
            for currency_code, exchange_rate in rates.items():
                # Get or create the currency record
                currency, created = Currency.objects.update_or_create(
                    name=currency_code,
                    defaults={'rates': exchange_rate}
                )
                
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Added new currency: {currency_code}"))
                else:
                    self.stdout.write(self.style.SUCCESS(f"Updated currency: {currency_code}"))

            self.stdout.write(self.style.SUCCESS("Currency rates successfully updated."))

        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f"Error fetching data from the API: {e}"))
