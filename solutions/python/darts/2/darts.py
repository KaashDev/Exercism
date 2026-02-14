def score(x, y):

    radius = (x**2 + y**2) ** 0.5
    # Booleans are integers
    # True = 1
    # False = 0
    return (radius<=1) * 5 + (radius<=5) * 4 + (radius<=10) * 1