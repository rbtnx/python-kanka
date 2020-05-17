"""
Main Kanka API functions and classes
"""
from datetime import datetime
from dacite import from_dict, Config
from .exceptions import KankaError
from .utils import KankaSession, to_datetime
from .objects.user import Profile, Campaign


class KankaClient(object):
    """
    Interact with kanka API with this client.
    """
    def __init__(self, token=''):
        self.session = KankaSession(api_token=token)

    def get_profile(self):
        """
        Get Profile information.
        """
        profile = Profile(self.session.api_request("profile")["data"])

        return profile

    def get_campaigns(self):
        """
        Get list of campaigns.
        """
        campaigns = self.session.api_request("campaigns")["data"]
        return [Campaign(c) for c in campaigns]

    def campaign(self, c_id=None):
        """
        Get information about a campaign.
        """
        if c_id is None:
            raise KankaError("Campaign id not specified.")

        endpoint = f'campaigns/{str(c_id)}'
        campaign = from_dict(
            data_class=Campaign,
            data=self.session.api_request(endpoint)["data"],
            config=Config(type_hooks={datetime: to_datetime}))
        campaign.__post_init__(api_token=self.session.token)

        return campaign
