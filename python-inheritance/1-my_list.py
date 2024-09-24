#!/usr/bin/python3
"""
Contains MyList class
"""


class MyList(list):
    """
    This class adds an additional method to display the sorted list
    """
    def print_sorted(self):
        """
        Method that displays the sorted list,
        without modifying the original list.
        """
        print(sorted(self))
