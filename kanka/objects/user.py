"""
:mod:`kanka.user` - User Profile and Campaigns
"""
import kanka.objects.core as core
from .base import KankaObject
from ..utils import to_datetime, append_from
from ..exceptions import KankaError

class Profile(KankaObject):
    """
    Kanka Profile information.
    """
    def __init__(self, data):
        self._avatar = data["avatar"]
        self._avatar_thumb = data["avatar_thumb"]
        self._locale = data["locale"]
        self._last_campaign_id = data["last_campaign_id"]
        self._is_patreon = data["is_patreon"]

        super(Profile, self).__init__(data)

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


class Campaign(KankaObject):
    """
    List of Campaigns the user has access to.
    """
    def __init__(self, data):
        self._locale = data["locale"]
        self._entry = data["entry"]
        self._image = data["image"]
        self._image_full = data["image_full"]
        self._image_thumb = data["image_thumb"]
        self._visibility = data["visibility"]
        self._created_at = to_datetime(data["created_at"])
        self._updated_at = to_datetime(data["updated_at"])
        self._members = [m["user"]["name"] for m in data["members"]["data"]]

        super(Campaign, self).__init__(data)
        self.session.base_url = self.session.base_url + "campaigns/" + str(self._id) + "/"

    def get_list_of(self, endpoint):
        """
        Get list of characters in given campaign.
        """
        charlist = append_from(self.session, [], self.session.base_url + endpoint)
        return list(map(lambda l: (l["name"], l["id"]), charlist))

    def character(self, c_id=None):
        """
        Get character of campaign by character ID.
        """
        if c_id is None:
            raise KankaError("No character ID provided.")
        return core.Character(self.session.api_request("characters/" + str(c_id))["data"])

    def location(self, l_id=None):
        """
        Get location of campaign by location ID.
        """
        if l_id is None:
            raise KankaError("No location ID provided.")
        return core.Location(self.session.api_request("locations/" + str(l_id))["data"])

    def family(self, f_id=None):
        """
        Get family of campaign by family ID.
        """
        if f_id is None:
            raise KankaError("No family ID provided")
        return core.Family(self.session.api_request("families/" + str(f_id))["data"])

    def organisation(self, o_id=None):
        """
        Get organisation of campaign by organisation ID.
        """
        if o_id is None:
            raise KankaError("No organisation ID provided")
        return core.Organisation(self.session.api_request("organisations/" + str(o_id))["data"])

    def item(self, i_id=None):
        """
        Get item of campaign by item ID.
        """
        if i_id is None:
            raise KankaError("No item ID provided")
        return core.Item(self.session.api_request("items/" + str(i_id))["data"])

    def note(self, n_id=None):
        """
        Get note of campaign by note ID.
        """
        if n_id is None:
            raise KankaError("No note ID provided")
        return core.Note(self.session.api_request("notes/" + str(n_id))["data"])

    def race(self, r_id=None):
        """
        Get race of campaign by race ID.
        """
        if r_id is None:
            raise KankaError("No race ID provided")
        return core.Race(self.session.api_request("races/" + str(r_id))["data"])

    def quest(self, q_id=None):
        """
        Get quest of campaign by quest ID.
        """
        if q_id is None:
            raise KankaError("No quest ID provided")
        temp_quest = core.Quest(self.session.api_request("quests/" + str(q_id))["data"])
        temp_quest.session = self.session
        return temp_quest

    @property
    def entry(self):
        """
        :return: HTML description of campaign
        :rtype: string
        """
        return self._entry

    @property
    def visibility(self):
        """
        :return: Visibility (public or private)
        :rtype: string
        """
        return self._visibility

    @property
    def created_at(self):
        """
        :return: Creation date
        :rtype: datetime
        """
        return self._created_at

    @property
    def updated_at(self):
        """
        :return: Last updated
        :rtype: datetime
        """
        return self._updated_at

    @property
    def members(self):
        """
        :return: Members of campaign
        :rtype: list
        """
        return self._members
