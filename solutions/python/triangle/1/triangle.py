def is_valid_triangle(sides):
    """
    Docstring for is_valid_triangle
    
    :param sides: [int] length of each side
    Returns True if triangle if aall sides are greater than zero and sum of two sides are greater than the last side
    """
    a, b, c = sides

    return (a + b >= c and b + c >= a and a + c >= b) and (a > 0 and b > 0 and c > 0)

def equilateral(sides):
    """
    Docstring for equilateral
    
    :param sides: [int] length of each side

    Return True is all sides are equal
    Else returns False
    """

    return (sides[0] == sides[1] == sides[2]) and is_valid_triangle(sides)

def isosceles(sides):
    """
    Docstring for isosceles
    
    :param sides: [int] length of each side

    Return True is two sides are equal(but not all three)
    Else returns False
    """

    return (sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]) and is_valid_triangle(sides)

def scalene(sides):
    """
    Docstring for scalene
    
    :param sides: [int] length of each side

    Return True is none of the sides are equal
    Else returns False
    """

    return (sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]) and is_valid_triangle(sides)