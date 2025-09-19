import math, random

gameState = True


def coinFlip():
    landsOn = random.random()
    if landsOn > 0.5:
        return "Heads"
    else:
        return "Tails"


while gameState == True:
    headCount = 0
    timesTossed = 0
    points = 0
    while timesTossed < 11:
        output = coinFlip()
        if output == "Heads":
            headCount += 1
        timesTossed += 1
        print(timesTossed)

    if timesTossed >= 11:
        replayOrNo = input(
            "Input Y to play again. Input any other key to exit the program: "
        ).upper()
        if replayOrNo == "Y":
            timesTossed = 0
        else:
            gameState == False
            break
