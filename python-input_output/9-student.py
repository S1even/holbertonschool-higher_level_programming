#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Instantiation of the class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return self.__dict__
