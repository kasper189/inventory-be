# pylint: disable=invalid-name
# pylint: disable=no-member

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

        if keys.ID_KEY in item:
            self.id = item["id"]
            LOGGER.info("ID found: %s", self.id)
        else:
            LOGGER.info("ID not found")

    def get_dictionary(self):
        """Transforms an inventory item as bson to a dictionary.

            Returns:
                dict: the item as dictionary.
        """
        payload = dict()
        if hasattr(self, 'id'):
            payload[keys.ID_KEY] = str(self.id)
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


class UpdatorItem(object):
    """Item used to update inventory item.

        Attributes:
            id (str): item id that has to be updated.
        """
    def __init__(self, item_id):
        self.item_id = item_id

    def update(self, count):
        """Updates the item.

            Returns:
                item: the updated item.
        """
        LOGGER.info("Updating item %s with count %s",
                    str(self.item_id), str(count))
        DbItem.objects(id=self.item_id).update_one(set__count=count)
        json_item = JsonItem(DbItem.objects(id=self.item_id).first())
        return json_item.get_dictionary()
