"""
Main Kanka API functions and classes
"""
import requests
from .exceptions import KankaError
from .objects.user import Profile, Campaign

class KankaClient(object):
    """
    Interact with kanka API with this client.
    """
    def __init__(self, token=''):
        self._api_endpoint = 'https://kanka.io/api/1.0/'
        self._token = token

        if self._token  == '':
            raise KankaError("No token given")
        self._headers = {
            'Authorization': f'Bearer {self._token}',
            'Accept': 'application/json'}

    def _request(self, endpoint):
        url = self._api_endpoint + endpoint
        r = requests.get(url, headers=self._headers)
        return r.json()

    def get_profile(self):
        """
        Get Profile information.
        """
        profile = Profile(self._request("profile")["data"])

        return profile

    def get_campaigns(self):
        """
        Get list of campaigns.
        """
        campaigns = self._request("campaigns")["data"]
        return [Campaign(c) for c in campaigns]

    def campaign(self, c_id=None):
        """
        Get information about a campaign.
        """
        if c_id is None:
            raise KankaError("Campaign id not specified.")

        c = self._request("campaigns/" + str(c_id))
        return Campaign(c["data"])
