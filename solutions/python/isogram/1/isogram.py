def is_isogram(string):

    appeared = set()

    for letter in string.lower():
        if letter == " " or letter == "-":
            continue
        if letter in appeared:
            return False
        appeared.add(letter)

    return True