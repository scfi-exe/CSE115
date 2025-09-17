z = 43
x = 12
y = 14
if z < y:
    z = x
else:
    z = y
print(z)


def inf_O(outcome):
    if outcome == "fail":
        card = "red"
    else:
        card = "yellow"
    return card


print(inf_O("fail"))  # ER: red
print(inf_O("woaaaah"))  # ER: yellow


f_card = inf_O("test")
print(f_card)  # ER: yellow
