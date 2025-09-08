# distance between two values
def howFar(a, b):
    diff = a - b
    absVal = abs(diff)
    return absVal


result = howFar(6.5, 4.3)
print("Called howFar(6.5, 4.3)")
print(f"Expected Value: 2.2\nActual Value: {result}\n")

result = howFar(4.3, 6.5)
print("Called howFar(4.3, 6.5)")
print(f"Expected Value: 2.2\nActual Value: {result}")

result = howFar(8.4, 6.7)
print("Called howFar(8.4, 6.7)")
print(f"Expected Value: 1.7\nActual Value: {result}")
