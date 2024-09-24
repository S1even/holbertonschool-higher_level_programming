#!/usr/bin/env python3
"""Shapes, Interfaces, and Duck Typing"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Method to calculate the area of the shape."""

        pass

    @abstractmethod
    def perimeter(self):
        """Method to calculate the perimeter of the shape."""

        pass


class Circle(Shape):
    """Class representing a circle"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculates the area of the circle."""

        return pi * self._radius ** 2

    def perimeter(self):
        """Calculates the perimeter of the circle."""

        return 2 * pi * self.radius


class Rectangle(Shape):
    """Class representing a rectangle"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""

        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""

        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter"""

    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
