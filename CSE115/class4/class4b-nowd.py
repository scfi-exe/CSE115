import math


# write code to accept three numbers, [output1] express one to the power of the other and [output2] find the square root of the third number
# print the results
def calculator():
    while True:
        x = int(input("Enter the first integer: "))
        y = int(input("Enter the second integer: "))
        z = int(input("Enter the third integer: "))
        powerExp = math.pow(x, y)
        sqRoot = math.sqrt(z)
        print(f"{x} to the power of {x} = {powerExp}")
        print(f"The square root of {z} is: {sqRoot}\n")

        restart = input("Input Y to go again. Input any other key to exit the loop: ")
        if restart.lower() == "y":
            pass
        else:
            break


calculator()
