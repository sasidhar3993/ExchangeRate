import os
import yaml
import requests
import configparser


class BaseAPI:

    def __init__(self, api_id, hist_date=None, start_date=None, end_date=None) -> None:
        
        props = {}
        with open(os.path.dirname(__file__) + '/properties.yaml', 'r') as con:
             props = yaml.safe_load(con)

        conf = configparser.ConfigParser()
        conf.read(os.path.dirname(__file__) + '/conf.ini')
        self.url = conf.get('CONFIG', 'BASE_URL')
        self.access_key = conf.get('CONFIG', 'API_KEY')
        self.api_id = api_id
        self.props = props
        self.hist_date = hist_date
        self.start_date = start_date
        self.end_date = end_date
          
    def get_latest(self): 
        try:
            self.url = self.url + f"latest?access_key={self.access_key}"
            base = self.props[self.api_id].get('BASE')
            currency = self.props[self.api_id].get('CURRENCY')

            if base is not None: 
                self.url += f"& base={base}"       
            if currency is not None:
                self.url += f"& symbols={currency}"

            req = requests.get(self.url)
            req.raise_for_status()  # Raise an HTTPError for non-200 status codes

            data = req.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f"Request Error: {e}")
            return None
    
    def get_hist(self):
        try:
            self.url += f"{self.hist_date}?access_key={self.access_key}"
            base = self.props[self.api_id].get('BASE')
            currency = self.props[self.api_id].get('CURRENCY')

            if base is not None: 
                self.url += f"& base={base}"       
            if currency is not None:
                self.url += f"& symbols={currency}"

            req = requests.get(self.url)
            req.raise_for_status()  # Raise an HTTPError for non-200 status codes

            data = req.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f"Request Error: {e}")
            return None

    def get_time_series(self, start_date, end_date):
        pass
