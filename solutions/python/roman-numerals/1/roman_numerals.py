def roman(number):

    result = ""

    result += "M" * (number // 1000)
    number = number % 1000

    result += "D" * (number // 500)
    number = number % 500

    if number // 100 == 4:
        if "D" in result:
            result = result.replace("D", "CM")
        else:
            result += "CD"
    else:
        result += "C" * (number // 100)

    number = number % 100

    result += "L" * (number // 50)
    number = number % 50

    if number // 10 == 4:
        if "L" in result:
            result = result.replace("L", "XC")
        else:
            result += "XL"
    else:
        result += "X" * (number // 10)
    number = number % 10

    result += "V" * (number // 5)
    number = number % 5

    if number // 1 == 4:
        if "V" in result:
            result = result.replace("V", "IX")
        else:
            result += "IV"
    else:
        result += "I" * (number // 1)

    return result


