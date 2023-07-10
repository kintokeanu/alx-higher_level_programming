#!/usr/bin/python3

"""Defines an inherited list class MyList."""

def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if the object is exactly an
    instance of the specified class; False otherwise.
    """
    return type(obj) is a_class
