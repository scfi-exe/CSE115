# Define a function named largestOfFour that takes 4 numbers as parameters. The
# function should then return the largest of the four numbers.


def largestOfFour(num1, num2, num3, num4):
    return max(num1, num2, num3, num4)


# Test Cases:
# largestOfFour(1,2,3,4) should evaluate to 4
# largestOfFour(10,-1,-20,0) should evaluate to 10
# largestOfFour(4,4,1,4) should evaluate to 4

print(largestOfFour(1, 2, 3, 4))
print(largestOfFour(10, -1, -20, 0))
print(largestOfFour(4, 4, 1, 4))
print(largestOfFour(8, 16, 23, 42))  # 42
print(largestOfFour(1997, 2003, 1978, 2025))  # 2025
print(largestOfFour(2, 2, 5, 225))  # 225


# Define a function named squareFeet that takes 1 parameter, representing a number of gallons of paint (as an integer).
# It should return the total number of square feet that can be painted with that much paint, assuming that a gallon of paint
# covers 400 square feet.
def squareFeet(gal: int) -> int:
    return gal * 400


# Test Cases:
# squareFeet(1) should evaluate to 400
# squareFeet(4) should evaluate to 1600
# squareFeet(5) should evaluate to 2000
# squareFeet(10) should evaluate to 4000
# squareFeet(7) should evaluate to 2800
# squareFeet(8) should evaluate to 3200
print(squareFeet(1))
print(squareFeet(4))
print(squareFeet(5))
print(squareFeet(10))
print(squareFeet(7))
print(squareFeet(8))


# Define a function named classesCovered that takes 2 parameters, representing a number of gallons of paint and the size of a classroom
# in square feet (as integers). The function should return the number of classrooms of the given size that can be completely painted
# with the given amount of paint. Your function squareFeet should be used in this function to convert from gallons of paint to to sq. ft.


def classesCovered(gal: int, roomSize: int) -> int:
    sqftPaint = squareFeet(gal)
    roomsCovered = sqftPaint // roomSize
    return roomsCovered


# classesCovered(1,200) should evaluate to 2
# classesCovered(1,250) should evaluate to 1
# classesCovered(5,250) should evaluate to 8
# classesCovered(1,100) should evaluate to 4
# classesCovered(1,125) should evaluate to 3
# classesCovered(1,50) should evaluate to 8
print(classesCovered(1, 200))
print(classesCovered(1, 250))
print(classesCovered(5, 250))
print(classesCovered(1, 100))
print(classesCovered(1, 125))
print(classesCovered(1, 50))


# Define a function named removePunctuation that takes 1 parameter, a string. The function should return a copy of the
# input string but with all periods ('.'), commas (','), question marks ('?'), and exclamation points ('!') removed.


# def removePunctuation(txt=str) -> str:
#     txt = txt.replace(",", "")
#     txt = txt.replace(".", "")
#     txt = txt.replace("?", "")
#     txt = txt.replace("!", "")
#     return txt


# professors/ta's: i know you probably want us to solve it using something like the above code, but i wanted to try
# the below code to see if i could make it work. :)


def removePunctuation(txt: str) -> str:
    for punc in [".", ",", "?", "!"]:
        if punc in txt:
            txt = txt.replace(punc, "")
    return txt


# Test Cases:
# removePunctuation("Hello there!") should evaluate to "Hello there"
# removePunctuation("Harder, Better, Faster, Stronger") should evaluate to
# "Harder Better Faster Stronger".
# removePunctuation("Fullmetal Alchemist: Brotherhood") should evaluate to
# "Fullmetal Alchemist: Brotherhood"
print(removePunctuation("Hello there!"))
print(removePunctuation("Harder, Better, Faster, Stronger"))
print(removePunctuation("Fullmetal Alchemist: Brotherhood"))
print(
    removePunctuation("Hello, my name is Scott B. Finkelstein.")
)  # Hello my name is Scott B Finkelstein
print(removePunctuation("G.U.N.D.A.M."))  # GUNDAM
print(removePunctuation("D.N.A."))  # DNA


# Define a function named SHOUT that takes 1 parameter, a string. The function should return a copy of the input string but with all
# periods ('.'), commas (','), question marks ('?'), and exclamation points ('!') removed, all uppercase, and with three exclamation
# points added to the end. Your function removePunctuation should be used in this function to handle the removal of punctuation.
def SHOUT(txt: str) -> str:
    txt = removePunctuation(txt)
    txt = txt.upper() + "!!!"
    return txt


# the above code can also be written like this, using code from in-class:
# def SHOUT(txt=str) -> str:
#     txt = txt.replace(",", "")
#     txt = txt.replace(".", "")
#     txt = txt.replace("?", "")
#     txt = txt.replace("!", "")
#     txt = txt.upper() + "!!!"
#     return txt


print(SHOUT("Please sir, can I have some more?"))
print(SHOUT("Elementary, my dear Watson!"))
print(SHOUT("HELLO!!!!!!"))

# Test Cases:
# SHOUT("Please sir, can I have some more?") should return
# "PLEASE SIR CAN I HAVE SOME MORE!!!"
# SHOUT("Elementary, my dear Watson!") should return
# "ELEMENTARY MY DEAR WATSON!!!"
# SHOUT("HELLO!!!!!!") should return "HELLO!!!"
