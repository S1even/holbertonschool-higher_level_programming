#!/usr/bin/env python3
"""Shapes, Interfaces, and Duck Typing"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Class representing a geometric shape."""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Class representing a circle"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Class representing a rectangle"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter"""
    area = shape.area()
    perimeter = shape.perimeter()
    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))
