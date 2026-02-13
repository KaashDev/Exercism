def is_armstrong_number(number):
    """
    :param number:int - Number passed to check if it is an armstrong number

    Returns True if sum of each digit to the power of the length of number
    Else returns False
    """
    num = str(abs(number))

    power = len(num)
    
    sum_ = 0
    for digit in num:
        sum_ += int(digit) ** power

    return sum_ == number