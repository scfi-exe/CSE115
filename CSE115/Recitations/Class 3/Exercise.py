def twenty():
    return 20


def input_squared(dat):
    ret_val = dat**2
    return ret_val


def perimeter(length, width):
    result = (length * 2) + (width * 2)
    return result


# assign SQUARE the result of evaluating a functio ncall to PERMITER() using 3 and 5 as parameters
square = perimeter(3, 5)

# print the value returned when calling input_squared using 3.6 as it's argument
print(input_squared(3.6))

# assign left the result of evaluating a function call to twnety
# assign bottom the result of a function call to input_squared using [left] as its argument
# assign space the result of a function call to perimeter() with parameters [left] and [bottom]
left = twenty()
bottom = input_squared(left)
space = perimeter(left, bottom)
