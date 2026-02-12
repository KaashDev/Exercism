def square(number):

    """
    :param number: int - the current square
    
    Returns the number of grains on the given square
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)


def total():
    """
    Returns the number of grains on all 64 squares
    """
    total = 0
    for i in range(1, 65):
        total += square(i)

    return total

    