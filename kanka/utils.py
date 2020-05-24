"""
:mod: `kanka.utils` - Helper functions
"""

from datetime import datetime
from requests_toolbelt.sessions import BaseUrlSession
from requests_cache.core import CachedSession
from dacite import from_dict, Config
from .exceptions import KankaAPIError

API_BASE_ENDPOINT = 'https://kanka.io/api/1.0/'

class KankaSession(BaseUrlSession, CachedSession):
    """ Store session data.
    For every API request a header with the API token has to be provided.
    This object stores the token and the header and provides methods for
    GET, POST and UPDATE requests with the needed header. Also this object
    can be handed down from the KankaClient object to entitiy objects in case
    they need to make API requests.

    :param api_endpoint: Base endpoint to the kanka API. Default: API_BASE_ENDPOINT
    :param api_token: kanka API token. Default: empty string
    :type api_endpoint: string
    :type api_token: string
    """

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
        :return: json data from given endpoint
        :rtype: dict
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
    """ Convert json date entry to datetime.
    :param dict_date: Date as retrieved from kanka in the format "YYYY-mm-dd HH:MM:SS.000000"
    :type dict_date: string
    :return: Date converted to python datetime object
    :rtype: datetime.datetime
    """
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

def create_entity(Entity_object, data):
    """ Creates entitiy objects from dictionary. """
    entity = from_dict(
        data_class=Entity_object,
        data=data,
        config=Config(type_hooks={datetime: to_datetime}))
    return entity
