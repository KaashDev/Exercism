def is_pangram(sentence):
    """
    Docstring for is_pangram
    
    :param sentence: string - string passed to be checked
    Returns True is each letter(a-z) occurs atleast once in sentence.
    """
    alphabets = set(letter.upper() for letter in sentence if letter.isalpha())
    return len(alphabets) == 26