"""Database model for item in inventory.
"""
import logging
import mongoengine

import model.keys as keys

LOGGER = logging.getLogger()


class Item(object):
    """Db item for the inventory.

    Attributes:
        name (str): Human readable string describing the item.
        count (int): Number of items present in the inventory.
    """
    def __init__(self, name, count):
        LOGGER.info("Creating item with name %s and name %s", name, count)
        self.item = DbItem(name=name, count=count)

    def store(self):
        """Stores the element into the DB creating a new one.
        """
        LOGGER.info("Ready to store item in db")
        self.item.save()
        LOGGER.info("Element successfully added")


class DbItem(mongoengine.DynamicDocument):
    """Internal db item.
        An item is made up of:
        - name as string.
        - count as integer.
    """
    meta = {'collection': 'inventory'}
    name = mongoengine.StringField(max_lenght=60)
    count = mongoengine.IntField()


class JsonItem(object):
    """Json representation of inventory item.

        Attributes:
            item (obj): bson object read from db.
    """
    def __init__(self, item):
        if keys.NAME_KEY in item and keys.COUNT_KEY in item:
            self.name = item[keys.NAME_KEY]
            self.count = item[keys.COUNT_KEY]

    def get_dictionary(self):
        """Transforms an inventory item as bson to a dictionary.

            Returns:
                dict: the item as dictionary.
        """
        payload = dict()
        payload[keys.NAME_KEY] = self.name
        payload[keys.COUNT_KEY] = self.count

        return payload

    def get_name(self):
        """Getter method for name.

            Returns:
                str: the item name.
        """
        return self.name

    def get_count(self):
        """Getter method for count.

            Returns:
                str: the item count.
        """
        return self.count

