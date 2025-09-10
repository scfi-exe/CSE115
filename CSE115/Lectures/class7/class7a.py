def howFar(a, b):
    return abs(a - b)


result = howFar(4, 0)
# you should use test cases to test your code:
print(f"Called howFar(4,0)\nExpected Value: 4\nActual value: {result}\n")
# howFar(4.7,2.2) should return 2.5
result = howFar(4.2, 2.2)
print(f"Called howFar(4.7,2.2)\nExpected Value: 2.5\nActual value: {result}\n")
# howFar(3,4) should return 1
result = howFar(3, 4)
print(f"Called howFar(3,4)\nExpected Value: 1\nActual value: {result}\n")
# howFar(-4,-2) should return 2
result = howFar(-4, -2)
print(f"Called howFar(-4,-2)\nExpected Value: 2\nActual value: {result}\n")
