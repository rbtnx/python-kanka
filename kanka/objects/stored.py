""" Objects to store downloaded information about entities."""

from dataclasses import dataclass
import kanka.objects.core as core
from .base import Entity

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
