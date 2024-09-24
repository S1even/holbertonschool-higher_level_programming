#!/usr/bin/python3
"""Module that defines a class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    BaseGeometry class that represents a rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes width and height
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
