# REVIEW: Which expressions are valid in the Python language?
# false #A--> should be False
# 72(36 + 28)  # B --> should be 72*(36+28)
"I am taking CSE 115"  # C
# "Prof looks" + (2**6) #D --> can't concatenate a String with an Int
4 * (45 - 2) + 334 - 4359  # E


# REVIEW: which expressions evaluate to 42?
x = 42
y = "42"
z = 6

print(x)  # 1 [correct]
print(y)  # 2 [incorrect; it's a string not an int]
print("x")  # 3 [incorrect]
print(z * 7)  # 4 [correct]
# print(7z) #5 [incorrect and invalid]
print("z * 7")  # 6 #incorrect, is a string
# ANSWER: 1, 4 are expressions that evaluate to 42print(7z) #5


# example 1: create a pythonccode to calculate the distance between two values.
# the calculation must be done inside of a function
# first: understanding the problem; what do we need to do to solve it?
def distanceBetween():
    num1 = int(input("What is the first integer?: "))
    num2 = int(input("What is the second integer?: "))
    distance = num1 - num2
    output = abs(distance)
    print(f"The difference between {num1} and {num2} is {output}")
    return output


distanceBetween()
