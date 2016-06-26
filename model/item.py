"""Database model for item in inventory.
"""
import logging
import mongoengine

import model.keys as keys

LOGGER = logging.getLogger()

class Item(object):
    """Db item for the inventory

    Attributes:
        name (str): Human readable string describing the item.
        count (int): Number of items present in the inventory.
    """
    def __init__(self, name, count):
        LOGGER.info("Creating item with name %s and name %d" % (name, count))
        self.item = DbItem(name=name, count=count)

    def store(self):
        """To do
        """
        pass


class DbItem(mongoengine.DynamicDocument):
    """Internal db item
        An item is made up of:
        - name as string
        - count as integer
    """
    meta = {'collection': 'inventory'}
    name = mongoengine.StringField(max_lenght=60)
    count = mongoengine.IntField()


class JsonItem(object):
    def __init__(self, item):
        if keys.NAME_KEY in item and keys.COUNT_KEY in item:
            self.name = item[keys.NAME_KEY]
            self.count = item[keys.COUNT_KEY]

    def get_dictionary(self):
        payload = dict()
        payload[keys.NAME_KEY] = self.name
        payload[keys.COUNT_KEY] = self.count

        return payload
