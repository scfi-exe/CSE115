# trace the following code
def magic(x):
    x = x + 1


def moreMagic(y):
    ret_val = y + 2
    return ret_val


value = 0
magic(value)
value = moreMagic(2)
value = moreMagic(value)
