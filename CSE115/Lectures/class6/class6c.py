# Example 2

# write a python code to calculate the average of three values. the calculation must be done inside of a function
# first -> understanding the problem: what do we need to do to solve it?
# 1) we need to know the three numbers (variables to store the numbers: x,y,z)
# 2) then, the calculation (sum all the numbers and divide by the total of the numbers)


def avgOfThree(x, y, z):
    average = (x + y + z) / 3
    return average


result = avgOfThree(3, 3, 3)
print(
    f"Called avgOfThree(3,3,3)\nThe expected result is 3.0\n The actual result is {result}\n"
)

result = round(avgOfThree(72, 26, 88), 2)
print(
    f"Called avgOfThree(72,26,88)\nThe expected result is 62.0\n The actual result is {result}\n"
)

result = round(avgOfThree(100, 123, 277.99), 2)
print(
    f"Called avgOfThree(100,123,277.99)\nThe expected result is 167.0\n The actual result is {result}\n"
)

result = round(avgOfThree(10.5, 15, 18.4), 2)
print(
    f"Called avgOfThree(10.5,15,18.4)\nThe expected result is 14.63\n The actual result is {result}\n"
)
