"""Database model for item in inventory.
"""
import mongoengine


class Item(object):
    """Db item for the inventory

    Attributes:
        name (str): Human readable string describing the item.
        count (int): Number of items present in the inventory.
    """
    def __init__(self, name, count):
        self.item = _DbItem(name=name, count=count)

    def store(self):
        """To do
        """
        pass


class _DbItem(mongoengine.Document):
    """Internal db item
        An item is made up of:
        - name as string
        - count as integer
    """
    name = mongoengine.StringField(max_lenght=60)
    count = mongoengine.IntField()
