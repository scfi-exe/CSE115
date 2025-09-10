# write a python program to do acceleration = velocity / time


def accelRate(velocity, time):
    return velocity / time


value = accelRate(60, 2)
print(f"Ran accelRate(60,2)\nExpected Result is 30.0\nReturned: {value}\n")

value = accelRate(100, 4)
print(f"Ran accelRate(100, 4)\nExpected Result is 25.0\nReturned: {value}\n")

value = accelRate(120, 60)
print(f"Ran accelRate(120,60)\nExpected Result is 2.0\nReturned: {value}\n")
