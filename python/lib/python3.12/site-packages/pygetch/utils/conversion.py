"""
Utilities for converting to/from a tuple of ords

(c) 2015 Matthew Cotton
"""

def ords(string):
    """Convert string to tuple of ints"""
    return tuple(ord(c) for c in string)

def chars(tup):
    """Convert tuple of ints to string"""
    return ''.join(chr(o) for o in tup)
