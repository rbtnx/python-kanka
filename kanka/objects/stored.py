""" Objects to store downloaded information about entities."""

from typing import List, Optional
from dataclasses import dataclass
import kanka.objects.core as core
from .base import Entity
from .user import Campaign

@dataclass(repr=False)
class StoredCharacter(core.Character, Entity):
    pass

@dataclass(repr=False)
class StoredLocation(core.Location, Entity):
    pass

@dataclass(repr=False)
class StoredOrganisation(core.Organisation, Entity):
    pass

@dataclass(repr=False)
class StoredNote(core.Note, Entity):
    pass

@dataclass(repr=False)
class StoredRace(core.Race, Entity):
    pass

@dataclass(repr=False)
class StoredQuest(core.Quest, Entity):
    pass

@dataclass(repr=False)
class StoredJournal(core.Journal, Entity):
    pass

@dataclass(repr=False)
class StoredFamily(core.Family, Entity):
    pass

@dataclass(repr=False)
class StoredCampaign():
    name: str
    id: int
    entry: Optional[str] = None
    characters: Optional[List[StoredCharacter]] = None
    locations: Optional[List[StoredLocation]] = None
    organisations: Optional[List[StoredOrganisation]] = None
    notes: Optional[List[StoredNote]] = None
    races: Optional[List[StoredRace]] = None
    quests: Optional[List[StoredQuest]] = None
    journals: Optional[List[StoredJournal]] = None
    families: Optional[List[StoredFamily]] = None
