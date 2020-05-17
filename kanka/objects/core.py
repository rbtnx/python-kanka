"""
:mod: kanka.core
"""

from typing import Optional
from dataclasses import dataclass
from .base import Entity

@dataclass(repr=False)
class Character(Entity):
    location_id: Optional[int]
    title: Optional[str]
    age: Optional[int]
    sex: Optional[str]
    race_id: Optional[int]
    type: Optional[str]
    family_id: Optional[int]
    is_dead: bool
