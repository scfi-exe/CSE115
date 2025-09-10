def mystery(a, b, z):
    val = (a + b) - z
    print(f"val: {val}")
    print(f"returns: {val+1}")
    return val + 1


fst = mystery(1, 2, 3)  # val=0, return=1
snd = mystery(fst, 3, 2)  # val=2, return = 3
thd = mystery(fst, snd, 1)  # val =

# which is not a vlaue that val gets assigned
