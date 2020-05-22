"""
:mod:`kanka.user` - User Profile and Campaigns
"""

from dataclasses import dataclass, asdict
from datetime import datetime
import kanka.objects.core as core
from .base import KankaObject
from ..exceptions import KankaError
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

    def search(self, expression=None):
        """ Search for entities in the campaign.
        This function uses the /search/{expression} endpoint of the kanka API.
        Requesting from this endpoint returns entities with matching expressions
        inside the name field. It seemes that a maximum of ten matching entites are
        returned with every request (todo: verify). The search is not case sensitive.

        :param expression: Term to search for. Doesn't need to match the entity name
                            commpletly, can contain parts of the name
        :type expression: string
        :return: List of entities with matched names
        """
        if expression:
            match = []
            data = self.session.api_request(f'search/{str(expression)}')
            for item in data["data"]:
                match.extend([getattr(self, item["type"])(item["id"])])
            return match
        raise KankaError("An error occured.")

    def delete(self, entity=None, id=None):
        """Deletes an entity."""
        for attr in [entity, id]:
            if attr is None:
                raise KankaError("Missing either entity type or entity id.")
        url = self.session.base_url + f'{entity}s/{str(id)}'
        r = self.session.delete(url=url, headers=self.session.headers)
        if r.status_code == 204:
            return True
        return False

    def new_entity(self, entity=None):
        """ Creates new entity. """
        if entity:
            spawn = getattr(core, entity.title())(name=f'New {entity}', id=None)
            spawn.__post_init__(api_token=self.session.token)
            spawn.session.base_url = self.session.base_url + f'{entity}s'
            return spawn
        raise KankaError("No entity type given. Specify a type, ie new_entity(entity=\"location\"")
