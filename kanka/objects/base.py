"""
:mod: kanka.base
Base objects. Every object is derived fron KankaObject, 
every core entitiy is derived from Entity
"""

from datetime import datetime
from dataclasses import dataclass
from typing import Optional
from ..utils import KankaSession

@dataclass
class KankaObject:
    name: str
    id: Optional[int]

    def __post_init__(self, api_token=''):
        self.session = KankaSession(api_token=api_token)

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.name} (id: {self.id})'

    def __str__(self):
        return self.__repr__()

@dataclass(repr=False)
class Entity(KankaObject):
    image_thumb: str
    entity_id: int
    #tags: List[str]
    created_at: datetime
    created_by: int
    updated_at: datetime
    updated_by: int
    image_full: Optional[str] = None
    entry: Optional[str] = None
    is_private: Optional[bool] = None
    image: Optional[str] = None

@dataclass(repr=False)
class Trait(KankaObject):
    entry: str
    section: str
    is_private: bool
    default_order: int
