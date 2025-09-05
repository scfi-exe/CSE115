# prints and inputs go in the IO lines
# stack frames are for functinos that are defined in the LOC, NOT for native functions like print()

fahrenheit = 95
feels = "hot"
celsius = 35
kelvin = celsius
degrees = 3.1415
print("feels")
print(feels)
kelvin = 308.15


def ageCount():
    total = 0
    for age in range(4):
        age = int(input("What is your age?: "))
        total = total + age
    print(f"The combined total of the ages is: {total}")


ageCount()
