def rotate(text, key):
    
    letters = list(text)
    
    rotated = ""

    for letter in letters:
        asc = ord(letter)

        if letter.isupper():
            if asc + key > 90:
                asc = asc - 26
            rotated += chr(asc+key)
            continue

        if letter.islower():
            if asc + key > 122:
                asc = asc - 26
            rotated += chr(asc+key)
            continue

        rotated += letter

    return rotated
