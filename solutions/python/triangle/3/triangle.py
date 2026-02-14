def is_valid_triangle(sides):
    """
    Docstring for is_valid_triangle
    
    :param sides: [int] length of each side
    Returns True if triangle if aall sides are greater than zero and sum of two sides are greater than the last side
    """
    a, b, c = sorted(sides)

    return a + b > c and a > 0
    #The a > 0 check in is_valid_triangle is actually redundant. 
    #Since the sides are sorted, a is the smallest. So if a > 0, all sides are positive.

def equilateral(sides):
    """
    Docstring for equilateral
    
    :param sides: [int] length of each side

    Return True is all sides are equal(set automatically removes duplicates - 1 value left)
    Else returns False
    """

    return len(set(sides)) == 1 and is_valid_triangle(sides)

def isosceles(sides):
    """
    Docstring for isosceles
    
    :param sides: [int] length of each side

    Return True is two sides are equal(set automatically removes duplicates - 2 values left)
    Else returns False
    """

    return len(set(sides)) <= 2 and is_valid_triangle(sides)

def scalene(sides):
    """
    Docstring for scalene
    
    :param sides: [int] length of each side

    Return True is none of the sides are equal(no duplicates)
    Else returns False
    """

    return len(set(sides)) == 3 and is_valid_triangle(sides)