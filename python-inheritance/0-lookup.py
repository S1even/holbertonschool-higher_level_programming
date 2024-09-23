#!/usr/bin/python3
def lookup(obj):
    """
    This function returns a list of available attributes,
        and methods of a given object.

    Returns:
            list: A list containing the names of,
        the object's attributes and methods
    """
    return dir(obj)
