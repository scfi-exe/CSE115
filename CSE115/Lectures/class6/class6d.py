def avgOfThree():
    x = float(input("Please input the first number: "))
    y = float(input("Please input the second number: "))
    z = float(input("Please input the third number: "))
    average = round((((x + y + z) / 3)), 2)
    print(f"The average of {x}, {y}, and {z} is: {average}")
    return average


avgOfThree()
