#!/usr/bin/python3
"""
Module:1-rectangle
empty class that defines a rectangle
"""


class Rectangle:
    """
    This class represents a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle object with optional width and height.
        The default values are 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Getter method to retrieve the width of the rectangle.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        setter method to set the width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter method to retrieve the height of the rectangle
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Setter method to set the height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
