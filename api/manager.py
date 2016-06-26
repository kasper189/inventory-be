# pylint: disable=R0201
# pylint: disable=maybe-no-member

"""Api manager module.
"""
import logging

from flask_restful import Resource

import model.item as item
import manipulation.inventory


LOGGER = logging.getLogger()


class InventoryManager(Resource):
    """Inventory manager to handle api resources.
    """

    def get(self):
        """Get method for the inventory api.

            Returns:
                items (list): inventory item list.
            """
        LOGGER.debug("Get Inventory")
        inventory = item.DbItem.objects

        items = manipulation.inventory.build_inventory(inventory)

        return items
