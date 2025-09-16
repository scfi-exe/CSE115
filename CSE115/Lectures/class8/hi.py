def mystery(x, y):
    s = "A"

    if x < y:
        s = s + "B"

    s = s + "C"
    return s


print(mystery(7, 3))
