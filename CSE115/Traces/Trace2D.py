def better_score(x, y):
    sum = x + y
    higher_score = max(x, y)
    return higher_score


def lower_score(x, y):
    sub = x - y
    return min(x, y)


def match_grade(course, grade1, grade2):
    highest = better_score(grade1, grade2)
    lowest = lower_score(grade1, grade2)
    print("Highest grade in " + course + ": " + str(highest))
    print("Lowest grade in " + course + ": " + str(lowest))
    course = "CSE 199"
    return highest


course = "CSE 115"
midterm = 32
final = 100
best_grade = match_grade(course, midterm, final)
print(f"Course variable, after running the function, is: {course}")

print(5 + 12.00)


def bPrice(x):
    print(x)


bPrice(5.00)

print(38 * 1.08)
