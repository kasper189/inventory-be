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
