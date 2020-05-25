"""
Main Kanka API functions and classes
"""
from dataclasses import dataclass, asdict
from datetime import datetime

import kanka.objects.stored as stored
import kanka.objects.core as core
from .exceptions import KankaError
from .utils import create_entity, KankaSession, append_from, pluralize
from .objects.base import KankaObject

entitylist = ["character", "location", "organisation", "note",
              "race", "quest", "journal", "family"]

def bind_method(entity):
    def _method(self, entity_id):
        if entity_id:
            endpoint = f'{entity}s/{str(entity_id)}'
            data = self.session.api_request(endpoint)["data"]
            classname = getattr(stored, f'Stored{entity.title()}')
            return create_entity(Entity_object=classname, data=data)
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
        self.session  = KankaSession(api_token=api_token)
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
            return spawn
        raise KankaError("No entity type given. Specify a type, ie new_entity(entity=\"location\"")

    def upload(self, new_entity):
        """ Uploads a **new** entity to the kanka server."""
        if new_entity.id is None:
            resp = self.session.post(
                url=f'{self.session.base_url}{pluralize(new_entity.__class__.__name__)}',
                headers=self.session.headers,
                data=asdict(new_entity))
            if resp.status_code == 201:
                return resp.json()

            return resp #else
        raise KankaError("This entity has an ID. Set it to None if it's a new entity to upload it.")
            

class KankaClient(object):
    """ Interact with kanka API with this client.
    
    This class stores the kanka API token in a session object (see `~utils.KankaSession`).
    Also provides methods to retrieve campain and profile data.
    """
    def __init__(self, token=''):
        self.session = KankaSession(api_token=token)

    def get_profile(self):
        """ Get Profile information."""
        profile = Profile(self.session.api_request("profile")["data"])

        return profile

    def get_campaigns(self):
        """ Get list of campaigns.

        This function requests data from https://kanka.io/api/1.0/campaigns.
        :return: Array with campaigns
        :rtype: List of `~objects.user.Campaign`
        """
        data = self.session.api_request("campaigns")["data"]
        campaigns = [create_entity(Campaign, cdata) for cdata in data]
        return campaigns

    def campaign(self, c_id=None):
        """ Get information about a campaign."""
        if c_id is None:
            raise KankaError("Campaign id not specified.")

        for entity in entitylist:
            _method = bind_method(entity)
            setattr(Campaign, entity, _method)
        endpoint = f'campaigns/{str(c_id)}'
        campaign = create_entity(Campaign, self.session.api_request(endpoint)["data"])
        campaign.__post_init__(api_token=self.session.token)

        return campaign

    def import_campaign(self, c_id=None):
        if c_id is None:
            raise KankaError("Campaign id not specified.")

        data = self.session.api_request(f'campaigns/{str(c_id)}')
        for entity in entitylist:
            if entity[-1] == "y":
                entity = entity.replace("y", "ie")
            endpoint = f'{entity}s'
            data["data"][endpoint] = append_from(self.session, [], f'campaigns/{str(c_id)}/{endpoint}')

        imported = create_entity(Entity_object=stored.StoredCampaign, data=data["data"])
        return imported
