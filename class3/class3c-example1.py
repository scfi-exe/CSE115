# write a python code that reads 2 integers as inputs and prints the result of them

while True:
    operator = input("Please select an operator (+, -, *, /): ")
    num1 = int(input("What is the first number you would like to input?: "))
    num2 = int(input("What is the second number you would like to input?: "))

    if operator == "+":
        total = num1 + num2
        print(f"The sum of {num1} and {num2} is {total}")
    elif operator == "-":
        total = num1 - num2
        print(f"The difference of {num1} and {num2} is {total}")
    elif operator == "*":
        total = num1 * num2
        print(f"The product of {num1} and {num2} is {total}")
    elif operator == "/":
        total = num1 / num2
        print(f"{num1} divided by {num2} is equal to {total}")
    else:
        print("Invalid input - please try again.")
