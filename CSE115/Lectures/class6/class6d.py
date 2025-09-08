def avgOfThree():
    x = float(input("Please input the first number: "))
    y = float(input("Please input the second number: "))
    z = float(input("Please input the third number: "))
    average = round((((x + y + z) / 3)), 2)
    print(f"The average of {x}, {y}, and {z} is: {average}")
    return average


# test with:
# x = 3.44
# y = 5.6789
# z = 1.23456789
# result = 3.45
avgOfThree()

# test with:
# x = 56.67
# y = 45.19
# z = 52.18
# result = 51.35
# avgOfThree()
