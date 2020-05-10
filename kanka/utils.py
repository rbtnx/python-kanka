"""
:mod: `kanka.utils` - Helper functions
"""

from datetime import datetime
from requests_toolbelt.sessions import BaseUrlSession
from .exceptions import KankaError

API_BASE_ENDPOINT = 'https://kanka.io/api/1.0/'

class KankaSession(BaseUrlSession):
    """
    Store session data.
    """
    def __init__(self, api_endpoint=API_BASE_ENDPOINT, api_token=''):
        self.base_url = api_endpoint
        self.token = api_token
        self.auth_header = {
            'Authorization': f'Bearer {self.token}',
            'Accept': 'application/json'}

        super().__init__()
        self.headers.update(self.auth_header)

    def api_request(self, endpoint=''):
        if self.token == '':
            raise KankaError("No token given")
        return self.get(endpoint).json()

    def __repr__(self):
        return "Kanka Session to {}".format(self.base_url)

def to_datetime(dict_date):
    """
    Convert json date entry to datetime.
    """
    t = dict_date.split(".")[0]
    return datetime.strptime(t, "%Y-%m-%dT%H:%M:%S")
