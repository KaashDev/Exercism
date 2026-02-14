"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.

# Doesn't matter what you put here. Chose integers as more efficient.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 0


def sublist(list_one, list_two):
    
    if list_one == list_two:
        return EQUAL
    if is_sublist(list_two, list_one):
        return SUPERLIST
    if is_sublist(list_one, list_two):
        return SUBLIST
    return UNEQUAL

def is_sublist(small, big):

    # Check if the smaller list is empty
    if not small:
        return True
    
    #Imagine how many times an list of size 2 can fit in a list of size 4 (4 - 2 = 2 + 1 = 3)
    for i in range(len(big) - len(small) + 1):
        # Take sections of the bigger list and see if it is equal to the smaller list
        if big[i:i+len(small)] == small:
            return True
    return False