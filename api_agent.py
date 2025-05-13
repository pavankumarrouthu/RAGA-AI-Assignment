import requests

class APIAgent:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_market_data(self, symbol):
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={self.api_key}"
        response = requests.get(url)
        return response.json()
