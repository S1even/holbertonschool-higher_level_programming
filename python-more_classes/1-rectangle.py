#!/usr/bin/python3
"""
This module defines a simple Rectangle class.
"""


class Rectangle:
    """
    A class used to represent a Rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Attributes:
            width (float or int): The width of the rectangle (default is 0).
            height (float or int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.width = height

    @property
    def width(self):
        """
        Retreive method for the width attribute.

        Returns:
            Float or int: The current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): The value to set as the width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retreive method for the height attribute.

        Returns:
            int: The current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): The value to set as the height of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
