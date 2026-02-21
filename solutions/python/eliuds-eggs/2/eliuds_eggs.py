def egg_count(display_value):
    """
    Docstring for egg_count
    
    :param display_value: int - Decimal value passed to be converted to integer
    Returns number of 1s in binary format of display_value

    ## Restrictions

    Keep your hands off that bit-count functionality provided by your standard library!
    Solve this one yourself using other basic tools instead.
    """
    remainders = ""

    # Convert value passed to binary
    while display_value != 0:
        remainders += str(display_value % 2)
        display_value = display_value // 2
    remainders = remainders[::-1]

    # Count number of 1s in binary value
    return remainders.count("1")
