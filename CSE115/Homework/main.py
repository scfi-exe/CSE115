# define a function, accuracy, that takes 2 parameters representing (a) # of throws and (b) # of hits
# the function should return accuracy as a percentage rounded to 1 decimal place


def accuracy(throws, hits):
    return round(((hits / throws) * 100), 1)


# print(accuracy(10, 5)) #UAT, should return 50.0


# define a function named onlyOs that takes a string and returns the same string, but with all vowels replaced by the leter "o"
# for the purposes of this function, you may assume that Y is not a vowel
def onlyOs(txt):
    txt = txt.replace("a", "o")
    txt = txt.replace("e", "o")
    txt = txt.replace("i", "o")
    txt = txt.replace("u", "o")
    return txt


# print(onlyOs("caterpie")) #UAT, should return cotorpoo


# define a function named totalLength that takes two strings as parameters
# the function should return the sum of the string lengths
def totalLength(str1, str2):
    return len(str1) + len(str2)


# print(totalLength("abra", "kadabra")) #UAT, should return 11


# define a function named fullSections that takes 2 parameters (1) the # of students and (2) the size of a full CSE115 section
# the function should compute the number of sections that can be filled
def fullSections(studentCount, sectionMax):
    return studentCount // sectionMax


# print(fullSections(314, 100)) #UAT, should return 3


# define a function named leftovers that takes 2 parameters (1) a # of students (2) the size of a full seciton of CSE115
# the function should compute the number of students leftover after creating as many full sections as possible
def leftovers(studentCount, sectionMax):
    return studentCount % sectionMax


# print(leftovers(314, 100)) #UAT, should return 14
