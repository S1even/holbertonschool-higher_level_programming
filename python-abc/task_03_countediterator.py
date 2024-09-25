#!/usr/bin/python3

class CountedIterator:
    """Iterator that counts how many items have been iterated over"""
    def __init__(self, iterable):
        self._iterator = iter(iterable)
        self._counter = 0

    def get_count(self):
        return self._counter

    def __next__(self):
        try:
            item = next(self._iterator)
            self._counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        return self
