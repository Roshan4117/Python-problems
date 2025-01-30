Weight = int(input(""))
water_lvl = input("")

if (0 < Weight <= 2000):# here weight is between 0 to 2000g so it will run on low water within 25 minutes
    if water_lvl == "L":
        timer = 25
    print("timer estimated:",timer)
elif (2000 < Weight <= 4000):# here weight is between 2001g to 4000g so it will run on medium water within 35 minutes
    if water_lvl == "M":# 
        timer = 35
    print("timer estimated",timer)
elif (4000 < Weight <= 7000):# here weight is between 4001 to 7000g so it will run on High water within 45 minutes
    if water_lvl == "H":
        timer = 45
    print("timer estimated:",timer)
elif (Weight > 7000):
    print("OVERLOAD")# here weight is over the maximum weight so it will overload and stop here and the rest is belowe 0 which is invalid 
elif ( Weight <= 0):
    print("Invalid")
else:
    print(" 0g 0 minutes") # if no inpput is given then it wont run at all 
