# pylint: disable=no-self-use
"""Post Api module.
"""
import logging
from flask_restful import reqparse
import error.exception as exception
import model.keys as keys

LOGGER = logging.getLogger()

class PutParser(object):
    """Class responsible of parsing the put request.
    """

    def parse(self):
        """Parses the PUT request.

            Returns:
                count (int): new item count.
        """
        LOGGER.info("Parsing put element")
        parser = reqparse.RequestParser()
        parser.add_argument(keys.COUNT_KEY, type=str, help='Item count')
        args = parser.parse_args()

        _count = args[keys.COUNT_KEY]

        if _count is not None:
            LOGGER.error("Parsed element without count")
        else:
            raise exception.BadItemFormat("Parsed item without count")

        return _count
