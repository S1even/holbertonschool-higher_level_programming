#!/usr/bin/python3
"""Module that defines a class BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class representing a square.
    """
    def __init__(self, size):
        """
        Initializes a new square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates the area of the square.
        """
        return self.__size * self.__size
