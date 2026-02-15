def rebase(input_base, digits, output_base):
    
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    if not digits or sum(digits) == 0:
        return [0]
    
    for x in digits:
        if x < 0 or x >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base") 

    base_ten = 0
    for digit in digits:
        base_ten = base_ten * input_base + digit

    remainders = list()

    while base_ten != 0:
        base_ten, rem = divmod(base_ten, output_base)
        remainders.append(rem)

    remainders.reverse()
    return remainders