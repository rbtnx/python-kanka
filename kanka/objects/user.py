"""
:mod:`kanka.user` - User Profile and Campaigns
"""

from dataclasses import dataclass
from datetime import datetime
from .base import KankaObject
from ..utils import append_from

@dataclass(repr=False)
class Profile(KankaObject):
    """ Kanka user profile information."""
    avatar: str
    avatar_thumb: str
    locale: str
    timezone: str
    date_formate: str
    default_pagination: int
    last_campaign_id: int
    is_patreon: bool

@dataclass(repr=False)
class Campaign(KankaObject):
    """ Holds information about a campaign."""
    locale: str
    entry: str
    image: str
    image_full: str
    image_thumb: str
    visibility: str
    created_at: datetime
    updated_at: datetime

    def __post_init__(self, api_token=''):
        super().__post_init__(api_token=api_token)
        self.session.base_url += f'campaigns/{str(self.id)}/'

    def get_list_of(self, endpoint):
        charlist = append_from(self.session, [], self.session.base_url + endpoint)
        return list(map(lambda l: (l["name"], l["id"]), charlist))
