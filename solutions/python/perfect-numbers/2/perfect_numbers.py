def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    sum_factors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_factors += i
    
    if number == sum_factors:
        return "perfect"
    if number < sum_factors:
        return "abundant"
    return "deficient"