import math


def areaOfCircle(r):
    area = math.pi * math.pow(r, 2)
    return area


r = float(input("Enter the radius: "))
area = round(areaOfCircle(r), 2)
print(f"The area of the circle is {area}")
