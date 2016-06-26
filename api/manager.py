from flask_restful import Resource

import model.item as item
import manipulation.inventory
import logging


LOGGER = logging.getLogger()


class InventoryManager(Resource):

    def get(self):
        LOGGER.debug("Get Inventory")
        inventory = item.DbItem.objects

        items = manipulation.inventory.build_inventory(inventory)

        return items
