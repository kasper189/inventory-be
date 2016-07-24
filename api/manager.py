# pylint: disable=R0201
# pylint: disable=maybe-no-member

"""Api manager module.
"""
import logging

from flask_restful import Resource

import error.exception as exception
import model.item as item
import manipulation.inventory
import api.post_parser as post_parser


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

    def post(self):
        """Post method for the inventory api.

        Returns:
            items (dict): newly added inventory item.
        """
        LOGGER.debug("Post Inventory")

        parser = post_parser.PostParser()
        try:
            dbitem = parser.parse()
            LOGGER.debug("Ready to inject element")
            dbitem.store()

            json_item = item.JsonItem(dbitem.item)
            return json_item.get_dictionary()

        except exception.BadItemFormat as bad_format:
            print bad_format
            return {"message": "error"}
