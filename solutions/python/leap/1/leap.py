def leap_year(year):
    """
    Docstring for leap_year
    
    :param year: int - year

    Returns True if year is divisible by 4 or if divisible and by both 100 and 400
    """

    return (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)
