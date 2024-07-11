import unittest
import requests

class TestOpenBreweryDB(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://api.openbrewerydb.org/breweries"

    def test_breweries_in_states(self):
        states = ['alaska', 'maine', 'new york']
        for state in states:
            response = requests.get(f"{self.base_url}?by_state={state}")
            breweries = response.json()
            brewery_names = [brewery['name'] for brewery in breweries]
            print(f"Breweries in {state.capitalize()}:")
            print("\n".join(brewery_names))
            print()

    def test_breweries_count_per_state(self):
        states = ['alaska', 'maine', 'new york']
        for state in states:
            response = requests.get(f"{self.base_url}?by_state={state}")
            breweries = response.json()
            print(f"Number of Breweries in {state.capitalize()}: {len(breweries)}")

    def test_breweries_by_city_count(self):
        states = ['alaska', 'maine', 'new york']
        for state in states:
            response = requests.get(f"{self.base_url}?by_state={state}")
            breweries = response.json()
            city_count = {}
            for brewery in breweries:
                city = brewery.get('city', 'Unknown')
                city_count[city] = city_count.get(city, 0) + 1
            print(f"Number of Breweries by City in {state.capitalize()}:")
            for city, count in city_count.items():
                print(f"{city}: {count}")

    def test_breweries_with_websites(self):
        states = ['alaska', 'maine', 'new york']
        for state in states:
            response = requests.get(f"{self.base_url}?by_state={state}")
            breweries = response.json()
            websites_count = 0
            for brewery in breweries:
                website = brewery.get('website_url', '')
                if website:
                    websites_count += 1
            print(f"Number of Breweries with Websites in {state.capitalize()}: {websites_count}")


if __name__ == '__main__':
    unittest.main()