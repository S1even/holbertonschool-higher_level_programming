#!/usr/bin/python3
"""Exact same object."""


def is_same_class(obj, a_class):
    """
    Function that checks if an object is,
    exactly an instance of the given class.

    Args:
        obj: The object to check.
        a_class: The class which we want to compare.

    Returns:
        True if the object is exactly an instance,
            of the given class, otherwise False.
    """
    return type(obj) == a_class
