# it will add two numbers and return the value
def sumTwoValues(num1, num2):
    total = num1 + num2
    return total


print(sumTwoValues(5, 5))
print(sumTwoValues(7, 8))
print(sumTwoValues(30, 12))
print(sumTwoValues(20, 3))


# it will take two user inputs and then sum them together
def sumTwoInputs():
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))

    total = num1 + num2
    print(f"The sum of {num1} + {num2} = {total}")
    return total


sumTwoInputs()
