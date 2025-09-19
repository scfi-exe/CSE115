def mystery(x, y, z):
    result = "X"
    if x < y:
        if x < z:
            result = result + "Y"
    else:
        result = result + "Z"
    return result


print(mystery(0, 1, -1))


def mystery(x, y, z):
    result = "X"
    if x < y:
        if x < z:
            result = result + "Y"
    else:
        result = result + "Z"
    return result


print(mystery(0, 1, -1))
