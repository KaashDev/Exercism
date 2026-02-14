def is_valid(isbn):
    """
    Docstring for is_valid
    
    :param isbn: int - sequence of alphanumeric characters passed to be checked for ISBN-10

    Returns True if isbn adheres to all rules of ISBN-10 convention.
    """
    if not isbn:
        return False
    
    values = list(isbn.replace("-",""))
    
    if len(values) != 10:
        #Checks if length of isbn is 10
        return False
    
    values_int = []
    for i, x in enumerate(values):
        if x == 'X':
            if i != 9:
                #Checks whether X is the last value(check digit)
                return False
            values_int.append(10)
        elif x.isdigit():
            values_int.append(int(x))
        else:
            return False
        
    return sum(values_int[i] * (10-i) for i in range(10)) % 11 == 0

