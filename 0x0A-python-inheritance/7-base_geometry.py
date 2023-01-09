#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsent base geometry."""

    def __init__(self):
        """initialize class"""
        pass

    def area(self):
        """Rasie Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer."""
        if not isinstance (value, int):
            raise TypeError ("{} must be an integer".format(name))
        
        if value <= 0:
            raise ValueError("{} must be grater than 0".format(name))
	
