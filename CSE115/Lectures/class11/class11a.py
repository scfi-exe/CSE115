# exercise 1
# - A game of coin tossing; every player gets a point for participation
# - A player gets an **additional 10 points if it comes down to head in nothing less than five times in ten throws**
# - Write python code to determine what a player gets at any time
import math, random

timesTossed = 0
headCount = 0
points = 0


def coinFlip():
    headsOrTails = random.random()
    if headsOrTails < 0.5:
        return "Tails"
    else:
        return "Heads"


while timesTossed < 10:
    landsOn = coinFlip()
    print(f"\n{landsOn}")
    if landsOn == "Heads":
        headCount += 1
    timesTossed += 1
    print(f"Times Tossed: {timesTossed}")


if headCount >= 5:
    points += 10
    print(
        f"\nYou landed on Heads {headCount} times in only 10 tosses. You earned 10 bonus points!\nPoints: {points}"
    )
else:
    points += 2
    print(
        f"\nYou landed on Heads {headCount} times in 10 tosses. You earned 2 bonus points!\nPoints: {points}"
    )

replayOrQuit = input(
    "Input Y to play again. Input any other key to exit the program"
).upper()

if replayOrQuit == "Y":
    timesTossed = 0
    headCount = 0

    while timesTossed < 10:
        landsOn = coinFlip()
        print(f"\n{landsOn}")
        if landsOn == "Heads":
            headCount += 1
        timesTossed += 1
        print(f"Times Tossed: {timesTossed}")

    if headCount >= 5:
        points += 10
        print(
            f"\nYou landed on Heads {headCount} times in only 10 tosses. You earned 10 bonus points!\nPoints: {points}"
        )
    else:
        points += 2
        print(
            f"\nYou landed on Heads {headCount} times in 10 tosses. You earned 2 bonus points!\nPoints: {points}"
        )
