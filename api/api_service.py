from typing import Any
import requests
import os
from .exception import ApiRequestException


class ApiService:
    def __init__(self) -> None:
        self.API_KEY = os.getenv('API_KEY')
        if not self.API_KEY:
            raise ValueError('Api Key is missing')

        self.BASE_URL = os.getenv('BASE_URL')
        self.HOST = os.getenv('HOST')
        self.headers: dict = {'x-rapidapi-key': self.API_KEY, 'x-rapidapi-host': self.HOST}
        

    # Fetch NFL data
    def fetch_nfl_data(self, season_year: int) -> dict[str, Any] | None:
        # Request data from api
        try:
            response = requests.get(
                    f'{self.BASE_URL}',
                    headers=self.headers,
                    params= {'year': season_year},
                    timeout = 10
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            raise ApiRequestException(str(e), response.status_code)
        except requests.exceptions.ConnectionError as e:
            raise ApiRequestException(f'Connection Error: {e}', None) 
        except requests.exceptions.Timeout as e:
            raise ApiRequestException(f'Timeout Error: {e}', None) 
        except requests.exceptions.RequestException as e:
            raise ApiRequestException(f'Requst Error: {e}', None)    

        return None