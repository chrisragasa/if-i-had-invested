import requests
import json

class AlphaVantageAPI:
    def __init__(self, ticker=""):
        self.apikey = "JQFUK84U8Y69YDYX"
        self.baseurl = "https://www.alphavantage.co/query?function="
        self.ticker = ticker
        self.res = {}
    
    def get_apikey(self):
        return self.apikey

    def get_baseurl(self):
        return self.baseurl

    def get_ticker(self):
        return self.ticker

    def get_data(self):
        return self.res
    
    def set_data(self, data):
        self.res = data

    def get_TIME_SERIES_DAILY(self):
        """Calls the Alpha Vantage TIME_SERIES_DAILY API

        Post Conditions:
            The res attribute of this object instance will be filled with the response from the API call.
            The response from the API call will be in JSON format and will contain an error message or
            the requested stock data.
        
        API Documentation:
            https://www.alphavantage.co/documentation/
        """
        fullurl = self.baseurl + "TIME_SERIES_DAILY&symbol=" + self.get_ticker() + "&apikey=" + self.get_apikey()
        #print(fullurl)
        r = requests.get(fullurl)
        r_json = json.loads(r.text)
        self.set_data(r_json)
        return self.get_data()

    def get_TIME_SERIES_MONTHLY(self):
        """Calls the Alpha Vantage TIME_SERIES_MONTHLY API

        Post Conditions:
            The res attribute of this object instance will be filled with the response from the API call.
            The response from the API call will be in JSON format and will contain an error message or
            the requested stock data.
        
        API Documentation:
            https://www.alphavantage.co/documentation/
        """
        fullurl = self.baseurl + "TIME_SERIES_MONTHLY&symbol=" + self.get_ticker() + "&apikey=" + self.get_apikey()
        #print(fullurl)
        r = requests.get(fullurl)
        r_json = json.loads(r.text)
        self.set_data(r_json)
        return self.get_data()
    

