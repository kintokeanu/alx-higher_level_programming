#!/usr/bin/python3
import json
"""writes an object to a text file using JSON representation"""


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a JSON representation.

    Args:
        my_obj (object): The object to be written to the file.
        filename (str): The name of the file to
        write the JSON representation to.

    Returns:
        None

    Raises:
        None

    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
