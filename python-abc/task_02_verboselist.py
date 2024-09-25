#!/usr/bin/python3

class VerboseList(list):
    """A subclass of the built-in list that provides verbose output"""

    def append(self, item):
        """Adds item to the list and print the message"""
        print("Added [{}] to the list.".format(item))
        super().append(item)

    def extend(self, item):
        """Extend the lists with items"""
        print("Extends the list with [{}] items.".format(len(item)))
        super().extend(item)

    def remove(self, item):
        """Remove item from the list"""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop item from the list"""
        if self:
            pop_item = self[index]
            print("Popped [{}] from the list.".format(pop_item))
            return super().pop(index)
        else:
            raise ValueError("Cannot pop from an empty list.")
