# pylint: disable=no-self-use
"""Post Api module.
"""
import logging
from flask_restful import reqparse
import error.exception as exception
import model.keys as keys
import model.item as item

LOGGER = logging.getLogger()

class PostParser(object):
    """Class responsible of parsing the post request.
    """

    def parse(self):
        """Parses the POST request.

            Returns:
                dbitem (object): inventory item.
        """
        LOGGER.info("Parsing posted element")
        parser = reqparse.RequestParser()
        parser.add_argument(keys.NAME_KEY, type=str, help='Item name')
        parser.add_argument(keys.COUNT_KEY, type=str, help='Item count')
        args = parser.parse_args()

        _name = args[keys.NAME_KEY]
        _count = args[keys.COUNT_KEY]

        if _name is None:
            LOGGER.error("Parsed element without name")
        if _count is None:
            LOGGER.error("Parsed element without count")

        if _name is not None and _count is not None:
            dbitem = item.Item(_name, _count)
            return dbitem
        else:
            LOGGER.info("THERE")
            raise exception.BadItemFormat("Parsed item without all fields")
