"""
Contains classes for the different entities.
"""

from .base import Entity, Trait

class Character(Entity):
    """
    Charakter entity.
    """
    def __init__(self, data):
        self._location_id = data["location_id"]
        self._title = data["title"]
        self._age = data["age"]
        self._sex = data["sex"]
        self._race_id = data["race_id"]
        self._type = data["type"]
        self._family_id = data["family_id"]
        self._is_dead = data["is_dead"]

        traits = data["traits"]["data"]
        self._traits = [Trait(t) for t in traits]

        super(Character, self).__init__(data)

    def __repr__(self):
        return "Character: {} (id: {})".format(self._name, self._id)

    @property
    def location_id(self):
        """
        :return: ID of associated location
        :rtype: integer
        """
        return self._location_id

    @property
    def title(self):
        """
        :return: Title of character
        :rtype: string
        """
        return self._title

    @property
    def age(self):
        """
        :return: Age of character
        :rtype: integer
        """
        return self._age

    @property
    def sex(self):
        """
        :return: Sex of character
        :rtype: string
        """
        return self._sex

    @property
    def race_id(self):
        """
        :return: ID of character race
        :rtype: integer
        """
        return self._race_id

    @property
    def type(self):
        """
        :return: Character type (NPC, player, etc..)
        :rtype: string
        """
        return self._type

    @property
    def family_id(self):
        """
        :return: ID of associated family
        :rtype: integer
        """
        return self._family_id

    @property
    def is_dead(self):
        """
        :return: Determines if character is dead or not
        :rtype: boolean
        """
        return self._is_dead

    @property
    def traits(self):
        """
        :return: Character traits
        :rtype: list of KankaObject::Trait
        """
        return self._traits

class Location(Entity):
    """
    Location entity.
    """
    def __init__(self, data):
        self._parent_location_id = data["parent_localtion_id"]
        self._map = data["map"]
        self._type = data["type"]

        super(Location, self).__init__(data)

    def __repr__(self):
        return "Location: {} (id: {})".format(self._name, self._id)

    @property
    def parent_location_id(self):
        """
        :return: ID of parent location
        :rtype: integer
        """
        return self._parent_location_id

    @property
    def type(self):
        """
        :return: Location type
        :rtype: string
        """
        return self._type

    @property
    def map(self):
        """
        :return: Relative url to map
        :rtype: string
        """
        return self._map

class Family(Entity):
    """
    Family entity.
    """
    def __init__(self, data):
        self._location_id = data["location_id"]
        self._family_id = data["family_id"]

        members = data["members"]["data"]
        self._members = [Character(c) for c in members]

        super(Family, self).__init__(data)

    def __repr__(self):
        return "Family: {} (id: {})".format(self._name, self._id)

    @property
    def location_id(self):
        """
        :return: Location ID
        :rtype: integer
        """
        return self._location_id

    @property
    def family_id(self):
        """
        :return: Family ID
        :rtype: integer
        """
        return self._family_id

    @property
    def members(self):
        """
        :return: Family members
        :rtype: list of Entity::Character
        """
        return self._members

class Organisation(Entity): 
    """
    Organisation entity.
    """
    def __init__(self, data):
        self._location_id = data["location_id"]
        self._organisation_id = data["family_id"]
        self._type = data["type"]

        members = data["members"]["data"]
        self._members = [Character(c) for c in members]

        super(Organisation, self).__init__(data)

    def __repr__(self):
        return "Organisation: {} (id: {})".format(self._name, self._id)

    @property
    def location_id(self):
        """
        :return: Location ID
        :rtype: integer
        """
        return self._location_id

    @property
    def organisation_id(self):
        """
        :return: Organisation ID
        :rtype: integer
        """
        return self._organisation_id

    @property
    def type(self):
        """
        :return: Organisation type
        :rtype: string
        """
        return self._type

    @property
    def members(self):
        """
        :return: Family members
        :rtype: list of Entity::Character
        """
        return self._members

class Item(Entity):
    """
    Item entity.
    """
    def __init__(self, data):
        self._location_id = data["location_id"]
        self._character_id = data["character_id"]
        self._type = data["type"]

        super(Item, self).__init__(data)

    def __repr__(self):
        return "Item: {} (id: {})".format(self._name, self._id)

    @property
    def location_id(self):
        """
        :return: Location ID
        :rtype: integer
        """
        return self._location_id

    @property
    def character_id(self):
        """
        :return: Character ID
        :rtype: integer
        """
        return self._character_id

    @property
    def type(self):
        """
        :return: Item type
        :rtype: string
        """
        return self._type
