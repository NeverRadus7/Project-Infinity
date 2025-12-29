"""
This file contains functions for sensibly printing
text to the console.

The utilities allow you to re-write previously-written
text, all without worrying about newlines, etc.

(c) 2015 Matthew Cotton
"""

import os
import sys
import time

####################################
# META (unix)

def disable_echoing():
    """Disables echoing and the cursor"""
    os.system("stty -echo") # disables echoing
    os.system('tput civis') # disables cursor

def enable_echoing():
    """Enables echoing and the cursor"""
    os.system("stty echo")  # enables echoing
    os.system('tput cnorm') # enables cursor

####################################
# STDOUT

def printsl(string):
    """
    Prints the given string as
    UTF-8-encoded, and flushes STDOUT
    """
    sys.stdout.write(string.encode('utf-8'))
    sys.stdout.flush()

def printslow(string, dt=0.1):

    for char in string:
        printsl(char)
        time.sleep(dt)

def back(length):
    """
    Returns the command string to move the
    cursor back by <length> places
    """
    return '\b'*(length)

def s_and_back(string):
    """
    Returns the given string followed
    by the correct reset string
    """
    return string + back(len(string))

def back_and_s(string):
    """
    Returns the correct reset string
    followed by the given string
    """
    return back(len(string)) + string

def clear(length):
    """Returns a screen-wipe for the given length"""
    return s_and_back(' '*length)

####################################

def print_and_drop_cursor(str1, str2):
    printsl(str1 + str2 + back(len(str2)))

def print_and_drop_cursor_formatted(formatted_string):
    (str1, str2) = formatted_string.split("{}")
    printsl(str1 + str2 + back(len(str2)))
