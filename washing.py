Weight = int(input(""))
water_lvl = ("L","M","H")

if (0 < Weight <= 2000):
    timer = 25
    print("",Weight,water_lvl[0])
elif (2000 < Weight <= 4000):
    timer = 35
    print("",Weight,water_lvl[1])
elif (4000 < Weight <= 7000):
    timer = 45
    print("",Weight,water_lvl[2])
elif (Weight > 7000):
    print("OVERLOAD")
elif ( Weight <= 0):
    print("Invalid")
else:
    print(" 0g 0 minutes")
