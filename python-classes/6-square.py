#!/usr/bin/python3
"""
This module defines a simple Square class.
"""


class Square:
    """
    This class represents a geometric square with a given size.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with an optional size

        Arguments:
                size (int, optional): The size of the square. Defaults to 0
                position (tuple, optional): The position of the square (x, y)
                                            Defaults to (0, 0)
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
                int: The size of the side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Initializes the square with an optional size (the default is 0).

        Arguments:
            size (int): The new size of the square.

        Errors:
            TypeError: Raised if size is not an integer.

            ValueError: Raised if size is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
                tuple: The position of the square (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.

        Args:
            value (tuple): The new position of the square (x, y).

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
            ValueError: If any element of position is less than 0.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
                int: The area of the square (size^2).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character `#`. If size is 0, it prints an
        empty line. The position attribute determines the indentation from
        the left and top margins.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")

            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
