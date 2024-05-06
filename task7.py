
import requests

def fetch_countries_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        # Assuming the response contains JSON data
        json_data = response.json()

        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Example
url = "https://restcountries.com/v3.1/all"
countries_data = fetch_countries_data(url)

if countries_data:
    # Now we can work with the 'countries_data' variable, which contains the JSON data
    print(countries_data)
else:
    print("Failed to fetch data.")
import requests

def fetch_countries_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Assuming the response contains JSON data
        json_data = response.json()

        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_country_info(country_data):
    for country in country_data:
        name = country.get('name', {}).get('common', 'N/A')
        currencies = country.get('currencies', {})
        
        if currencies:
            print(f"Country: {name}")
            print("Currencies:")
            
            for currency_code, currency_info in currencies.items():
                currency_name = currency_info.get('name', 'N/A')
                currency_symbol = currency_info.get('symbol', 'N/A')
                
                print(f"  - Currency Code: {currency_code}")
                print(f"    Currency Name: {currency_name}")
                print(f"    Currency Symbol: {currency_symbol}")
            
            print("\n")

# Example usage
url = "https://restcountries.com/v3.1/all"
countries_data = fetch_countries_data(url)

if countries_data:
    display_country_info(countries_data)
else:
    print("Failed to fetch data.")
import requests

def fetch_countries_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Assuming the response contains JSON data
        json_data = response.json()

        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_countries_with_dollar_currency(country_data):
    for country in country_data:
        name = country.get('name', {}).get('common', 'N/A')
        currencies = country.get('currencies', {})
        
        # Check if the currency is "Dollar"
        if any(currency_code.lower() == 'usd' for currency_code in currencies):
            print(f"Country: {name}")
            print("Currencies:")
            
            for currency_code, currency_info in currencies.items():
                currency_name = currency_info.get('name', 'N/A')
                currency_symbol = currency_info.get('symbol', 'N/A')
                
                print(f"  - Currency Code: {currency_code}")
                print(f"    Currency Name: {currency_name}")
                print(f"    Currency Symbol: {currency_symbol}")
            
            print("\n")

# Example usage
url = "https://restcountries.com/v3.1/all"
countries_data = fetch_countries_data(url)

if countries_data:
    display_countries_with_dollar_currency(countries_data)
else:
    print("Failed to fetch data.")
import requests

def fetch_countries_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Assuming the response contains JSON data
        json_data = response.json()

        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_countries_with_euro_currency(country_data):
    for country in country_data:
        name = country.get('name', {}).get('common', 'N/A')
        currencies = country.get('currencies', {})
        
        # Check if the currency is "Euro"
        if any(currency_code.lower() == 'eur' for currency_code in currencies):
            print(f"Country: {name}")
            print("Currencies:")
            
            for currency_code, currency_info in currencies.items():
                currency_name = currency_info.get('name', 'N/A')
                currency_symbol = currency_info.get('symbol', 'N/A')
                
                print(f"  - Currency Code: {currency_code}")
                print(f"    Currency Name: {currency_name}")
                print(f"    Currency Symbol: {currency_symbol}")
            
            print("\n")

# Example usage
url = "https://restcountries.com/v3.1/all"
countries_data = fetch_countries_data(url)

if countries_data:
    display_countries_with_euro_currency(countries_data)
else:
    print("Failed to fetch data.")
import requests

def fetch_breweries_by_state(url, state):
    try:
        response = requests.get(url, params={'by_state': state})
        response.raise_for_status()

        # Assuming the response contains JSON data
        json_data = response.json()

        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def list_brewery_names_by_states(url, states):
    for state in states:
        print(f"Breweries in {state}:")
        breweries_data = fetch_breweries_by_state(url, state)

        if breweries_data:
            for brewery in breweries_data:
                brewery_name = brewery.get('name', 'N/A')
                print(f"  - {brewery_name}")
        else:
            print("Failed to fetch data.")

        print("\n")

# Example usage
url = "https://api.openbrewerydb.org/breweries"
states_of_interest = ['Alaska', 'Maine', 'New York']
list_brewery_names_by_states(url, states_of_interest)
import requests

def fetch_breweries_by_state(url, state):
    try:
        response = requests.get(url, params={'by_state': state})
        response.raise_for_status()

        # Assuming the response contains JSON data
        json_data = response.json()

        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def count_breweries_by_states(url, states):
    for state in states:
        breweries_data = fetch_breweries_by_state(url, state)

        if breweries_data:
            brewery_count = len(breweries_data)
            print(f"Number of breweries in {state}: {brewery_count}")
        else:
            print(f"Failed to fetch data for {state}.")

# Example usage
url = "https://api.openbrewerydb.org/breweries"
states_of_interest = ['Alaska', 'Maine', 'New York']
count_breweries_by_states(url, states_of_interest)
