# Consider choosing clothing for the day:
#     If the temp is above 80, you will wear shorts
#     But, when the temp is not above 80, you check if it is snowing
#         If it is SNOWING, you stay home in pajama pants
#         ELSE, you wear jeans
#     ALWAYS wear a tropical shirt


def chooseClothes(temp: int, snowing: bool) -> str:
    if temp > 80:
        print("Wearing shorts")
    else:
        if snowing == True:
            print("Staying in PJs")
        else:
            print("Putting on jeans")

    return "Wearing a tropical shirt"


print(chooseClothes(85, False))

print(chooseClothes(30, True))
