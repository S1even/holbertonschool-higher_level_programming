#!/usr/bin/python3
"""Define a function filename"""


def write_file(filename="", text=""):
    """
    Function that writes text to a file, creating it if it does not exist
    or by overwriting its content if it already exists.

    Args:
        filename (str): The name of the file to write to.
        Defaults to an empty string ("").

        text (str): The text to write to the file.
        Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
