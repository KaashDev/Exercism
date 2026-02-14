def convert(number):
    sounds = {3: "Pling", 5: "Plang", 7: "Plong"}
    result = ''.join(sound for factor, sound in sounds.items()
                     if number % factor == 0)
    return result or str(number)