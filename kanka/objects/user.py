"""
:mod:`kanka.user` - User Profile and Campaigns
"""

from dataclasses import dataclass
from datetime import datetime
from dacite import from_dict, Config
import kanka.objects.stored as stored
from .base import KankaObject
from ..utils import to_datetime, append_from
from ..exceptions import KankaError

def bind_method(entity):
    def _method(self, entity_id):
        if entity_id:
            endpoint = f'{entity}s/{str(entity_id)}'
            data = self.session.api_request(endpoint)["data"]
            classname = getattr(stored, f'Stored{entity.title()}')
            return from_dict(
                data_class=classname,
                data=data,
                config=Config(type_hooks={datetime: to_datetime}))
        raise KankaError("No character ID provided.")
    return _method

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

    def character(self, c_id=None):
        if c_id:
            endpoint = f'characters/{str(c_id)}'
            data = self.session.api_request(endpoint)["data"]
            return from_dict(
                data_class=stored.StoredCharacter,
                data=data,
                config=Config(type_hooks={datetime: to_datetime}))
        raise KankaError("No character ID provided.")
