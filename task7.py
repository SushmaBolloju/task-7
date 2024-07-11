import requests

class CountryData:
    def __init__(self, url):
        self.url = url
        self.data = self.fetch_data()

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data")
            return None

    def display_country_names(self):
        if self.data:
            print("Country Names:")
            for country in self.data:
                print(country.get("name", "N/A"))

    def display_currency_info(self):
        if self.data:
            print("\nCurrency Information:")
            for country in self.data:
                name = country.get("name", "N/A")
                currencies = country.get("currencies", [])
                if currencies:
                    print(f"Country: {name}")
                    for currency in currencies:
                        print(f"Currency: {currency.get('name', 'N/A')} | Symbol: {currency.get('symbol', 'N/A')}")

    def countries_with_dollars_currency(self):
        if self.data:
            print("\nCountries with Dollars Currency:")
            for country in self.data:
                currencies = country.get("currencies", [])
                for currency in currencies:
                    if currency.get('name') == 'United States Dollar':
                        print(country.get("name", "N/A"))
                        break

    def countries_with_euro_currency(self):
        if self.data:
            print("\nCountries with Euro Currency:")
            for country in self.data:
                currencies = country.get("currencies", [])
                for currency in currencies:
                    if currency.get('name') == 'Euro':
                        print(country.get("name", "N/A"))
                        break

url = "https://restcountries.com/v3.1/all"
country_data = CountryData(url)
country_data.display_country_names()
country_data.display_currency_info()
country_data.countries_with_dollars_currency()
country_data.countries_with_euro_currency()
