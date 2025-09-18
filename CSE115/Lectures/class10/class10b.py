# - In a soccer competition, card decisions are made for interactions
# - Yellow when an opponent is hit and fall
# - Red card is issued whe nopponent is hit and cry


def pullCard(outcome):
    if outcome == "hit and fall":
        card = "yellow"
    elif outcome == "hit and cry":
        card = "red"
    else:
        card = ""
    return card


def pullCard(input1, input2):
    inputList = [input1, input2]
    if "hit" in inputList:
        if "fall" in inputList:
            card = "yellow"
        elif "cry" in inputList:
            card = "red"
    return card


# in a soccer competition, if there is "hit", indicate infraction.
# if the infraction results in fall, give red card
# otherwise, give yellow card
# this is the worst fucking code i have ever seen in my life and this guy really had the nerve to write this on the whiteboard
# def pullCard(std):
#     if impact == "hit":
#         outcome = "infraction"
#     if infraction == "fall":
#         outcome = "yellow"
#     else:
#         outcome = "red"
