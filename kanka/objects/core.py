"""
:mod: kanka.core
"""

from typing import Optional, List
from dataclasses import dataclass
from .base import Trait, KankaObject

@dataclass(repr=False)
class Core(KankaObject):
    name: str
    tags: Optional[List[int]] = None
    is_private: Optional[bool] = None
    image: Optional[str] = None  # this is supposed to be a stream to image..
    image_url: Optional[str] = None


@dataclass(repr=False)
class Character(Core):
    location_id: Optional[int] = None
    title: Optional[str] = None
    age: Optional[int] = None
    sex: Optional[str] = None
    race_id: Optional[int] = None
    type: Optional[str] = None
    family_id: Optional[int] = None
    is_dead: Optional[bool] = None
    traits: Optional[List[Trait]] = None


@dataclass(repr=False)
class Location(Core):
    type: Optional[str] = None
    map: Optional[str] = None #change to stream
    map_url: Optional[str] = None
    is_map_private: Optional[int] = None
    parent_location_id: Optional[int] = None


@dataclass(repr=False)
class Organisation(Core):
    location_id: Optional[int] = None
    type: Optional[str] = None
    organisation_id: Optional[int] = None


@dataclass(repr=False)
class Note(Core):
    type: Optional[str] = None


@dataclass(repr=False)
class Race(Core):
    type: Optional[str] = None
    race_id: Optional[int] = None


@dataclass(repr=False)
class Quest(Core):
    type: Optional[str] = None
    quest_id: Optional[int] = None
    character_id: Optional[int] = None


@dataclass(repr=False)
class Journal(Core):
    type: Optional[str] = None
    date: Optional[str] = None
    character_id: Optional[int] = None


@dataclass(repr=False)
class Family(Core):
    location_id: Optional[int] = None
    family_id: Optional[int] = None


@dataclass(repr=False)
class Item(Core):
    type: Optional[str] = None
    location_id: Optional[int] = None
    character_id: Optional[int] = None


@dataclass(repr=False)
class Event(Core):
    type: Optional[str] = None
    date: Optional[str] = None
    location_id: Optional[int] = None


@dataclass(repr=False)
class Ability(Core):
    type: Optional[str] = None
    ability_id: Optional[int] = None
    charges: Optional[int] = None


@dataclass(repr=False)
class Conversation(Core):
    type: Optional[str] = None
    target: Optional[str] = None
