"""
Kanka entity python classes.
"""

from ..exceptions import KankaError
from ..utils import to_datetime

class KankaObject(object):
    """
    Kanka Object with name and id.
    """
    def __init__(self, data):
        for i in ["id", "name"]:
            if i not in data:
                raise KankaError("Missing {}. Couldn't create object.")
        self._id = data["id"]
        self._name = data["name"]

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
    """
    Base class with common attributes for all Entities as defined in the documentation. Although every field is
    always present, its value may be None.
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

    def __repr__(self):
        return "Entity: {} (id: {})".format(self._name, self._id)
    
    def __str__(self):
        return self.__repr__()
