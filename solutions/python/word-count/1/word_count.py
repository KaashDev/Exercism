import re
def count_words(sentence):
    
    sentence = sentence.lower().replace("@", "").replace("\n", "").replace("_", " ")
    words = re.split(r'[ ,\n\t]', sentence)

    map = {}
    for word in words:
        new_word = ""
        for i, letter in enumerate(word):
            if letter.isalpha() or letter.isdigit() or (letter == "'" and i > 0 and i < len(word) - 1 and word[i-1].isalpha() and word[i+1].isalpha()):
                new_word += letter
        if new_word != "":
            if new_word not in map:
                map[new_word] = 0
            map[new_word] += 1

    return map