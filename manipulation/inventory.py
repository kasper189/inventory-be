"""Manipulation module.
"""

import model.item as model

def build_inventory(bson_items):
    """Builds the inventory as dictionary element.

        Attributes:
            bson_items (list): List of bson object read from mongoDB.

        Returns:
            list: list of inventory item as dictionary.
        """
    item_list = list()

    for item in bson_items:
        json_item = model.JsonItem(item)
        item_list.append(json_item.get_dictionary())

    return item_list

