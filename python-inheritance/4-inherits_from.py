#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """
    Returns:
        True if obj is an instance of a subclass of a_class,
            but not a direct instance of a_class.
            Otherwise, False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
