def translate(text):

    vowels = 'aeiou'

    words = text.split()
    result = []

    for word in words:
        if word[0] in vowels or word.startswith(('xr', 'yt')):
            result.append(word + 'ay')
            continue

        i = 0

        while i < len(word):

            if word[i:i+2] == "qu":
                i = i + 2
                break

            if i > 0 and word[i] == "y":
                break

            if word[i] in vowels:
                break

            i += 1

        result.append(word[i:] + word[:i] + 'ay')

    return " ".join(result)
    


