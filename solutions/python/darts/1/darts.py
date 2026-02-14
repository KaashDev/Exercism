def score(x, y):

    if (x**2 + y**2) ** 0.5 <= 1:
        return 10
    if (x**2 + y**2) ** 0.5 <= 5:
        return 5
    if (x**2 + y**2) ** 0.5 <= 10:
        return 1
    return 0
