"""
:mod: `kanka.utils` - Helper functions
"""

from datetime import datetime
from requests_toolbelt.sessions import BaseUrlSession
from .exceptions import KankaAPIError

API_BASE_ENDPOINT = 'https://kanka.io/api/1.0/'

class KankaSession(BaseUrlSession):
    """ Store session data."""
    def __init__(self, api_endpoint=API_BASE_ENDPOINT, api_token=''):
        self.base_url = api_endpoint
        self.token = api_token
        auth_header = {
            'Authorization': f'Bearer {self.token}',
            'Accept': 'application/json'}

        super().__init__()
        self.headers.update(auth_header)

    def api_request(self, endpoint=''):
        """
        Requests data from given API endpoint.
        Returns json data on success.
        """
        r = self.get(endpoint)
        if r.status_code == 401:
            raise KankaAPIError("Authentication error. Wrong token or no token given.")
        if r.status_code == 404:
            raise KankaAPIError(
                "Page not found. Request from a non-existent endpoint: {}.".format(r.url))

        return r.json()

    def __repr__(self):
        return "Kanka Session to {}".format(self.base_url)

def to_datetime(dict_date):
    """ Convert json date entry to datetime."""
    t = dict_date.split(".")[0]
    return datetime.strptime(t, "%Y-%m-%dT%H:%M:%S")

def append_from(session, data, page):
    """ Collect paginated data."""
    r = session.api_request(page)
    url_next = r["links"]["next"]
    if url_next:
        append_from(session, data, url_next[len(session.base_url):])
    data.extend(r["data"])
    return data
