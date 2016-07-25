"""Exceptons module.
"""

class BadItemFormat(Exception):
    """Exception linked to item format.
        Attributes:
                args (str)
                kwargs (str)
    """

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

    def get_error_message(self):
        """Gets the exception error message.

            Returns:
                str: the error message.
        """
        return self.args
