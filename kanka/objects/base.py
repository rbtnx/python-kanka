"""
Kanka entity python classes.
"""

from ..exceptions import KankaError
from ..utils import to_datetime, KankaSession

class KankaObject():
    """
    Kanka Object with name and id.
    """
    def __init__(self, data):
        for i in ["id", "name"]:
            if i not in data:
                raise KankaError("Missing {}. Couldn't create object.")
        self._id = data["id"]
        self._name = data["name"]
        self.session = KankaSession()

    @property
    def id(self):
        """
        :return: id
        :rtype: integer
        """
        return self._id

    @property
    def name(self):
        """
        :return: name
        :rtype: string
        """
        return self._name

    def __repr__(self):
        return "Object name: {} (id: {})".format(self._name, self._id)

    def __str__(self):
        return self.__repr__()

class Entity(KankaObject):
    # pylint: disable=too-many-instance-attributes
    """
    Base class with common attributes for all Entities as defined in the documentation.
    Although every field is always present, its value may be None.
    """
    def __init__(self, data):
        self._entry = data["entry"]
        self._image = data["image"]
        self._image_full = data["image_full"]
        self._image_thumb = data["image_thumb"]
        self._is_private = data["is_private"]
        self._entity_id = data["entity_id"]
        self._tags = data["tags"]
        self._created_at = to_datetime(data["created_at"])
        self._created_by = data["created_by"]
        self._updated_at = to_datetime(data["updated_at"])
        self._updated_by = data["updated_by"]

        super(Entity, self).__init__(data)

    @property
    def entry(self):
        """
        :return: HTML description of entity
        :rtype: string
        """
        return self._entry

    @property
    def is_private(self):
        """
        :return: Determines if object is visible to admin members
        :rtype: boolean
        """
        return self._is_private

    @property
    def entity_id(self):
        """
        :return: identifying id against other entities
        :rtype: integer
        """
        return self._entity_id

    @property
    def tags(self):
        """
        :return: Tags to related objects
        :rtype: list
        """
        return self._tags

    @property
    def created_at(self):
        """
        :return: Creation date
        :rtype: datetime
        """
        return self._created_at

    @property
    def created_by(self):
        """
        :return: User id of creator
        :rtype: integer
        """
        return self._created_by

    @property
    def update_at(self):
        """
        :return: Update date
        :rtype: datetime
        """
        return self._updated_at

    @property
    def update_by(self):
        """
        :return: User id of user that last updated the entity
        :rtype: integer
        """
        return self._updated_by

    def __repr__(self):
        return "Entity: {} (id: {})".format(self._name, self._id)

    def __str__(self):
        return self.__repr__()

class Trait(KankaObject):
    """
    Trait object used by character entity.
    """
    def __init__(self, data):
        self._entry = data["entry"]
        self._section = data["section"]
        self._is_private = data["is_private"]
        self._default_order = data["default_order"]

        super(Trait, self).__init__(data)

    @property
    def entry(self):
        """
        :return: HTML description of entity
        :rtype: string
        """
        return self._entry

    @property
    def section(self):
        """
        :return: Which section the trait belongs to
        :rtype: string
        """
        return self._section


    @property
    def is_private(self):
        """
        :return: Determines if the trait in set private
        :rtype: boolean
        """
        return self._is_private

    @property
    def default_order(self):
        """
        :return: Ordering of trait
        :rtype: integer
        """
        return self._default_order

    def __repr__(self):
        return "Trait name: {} (id: {})".format(self._name, self._id)

    def __str__(self):
        return self.__repr__()
