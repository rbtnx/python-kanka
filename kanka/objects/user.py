"""
:mod:`kanka.user` - User Profile and Campaigns
"""
from ..utils import to_datetime

class Profile(object):
    """
    Profile information.
    """
    def __init__(self, data):
        self._id = data["id"]
        self._name = data["name"]
        self._avatar = data["avatar"]
        self._avatar_thumb = data["avatar_thumb"]
        self._locale = data["locale"]
        self._last_campaign_id = data["last_campaign_id"]
        self._is_patreon = data["is_patreon"]
    
    @property
    def id(self):
        """
        :return: id
        :rtype: integer
        """
        return self._id

    @property
    def name(self):
        """
        :return: name
        :rtype: string
        """
        return self._name

    @property
    def last_campaign_id(self):
        """
        :return: id of last campaign
        :rtype: integer
        """
        return self._last_campaign_id
    
    @property
    def is_patreon(self):
        """
        :return: Patreon flag
        :rtype: Boolean
        """
        return self._is_patreon

    def __repr__(self):
        return "User: {} (id: {})".format(self._name, self._id)

    def __str__(self):
        return self.__repr__()


class Campaign(object):
    """
    List of Campaigns the user has access to.
    """
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.locale = data["locale"]
        self.entry = data["entry"]
        self.image = data["image"]
        self.image_full = data["image_full"]
        self.image_thumb = data["image_thumb"]
        self.visibility = data["visibility"]
        self.created_at = to_datetime(data["created_at"])
        self.updated_at = to_datetime(data["updated_at"])
        self.members = [m["user"]["name"] for m in data["members"]["data"]]

    def __repr__(self):
        return "Name: {} (id: {})".format(self.name, self.id)

    def __str__(self):
        return self.__repr__()