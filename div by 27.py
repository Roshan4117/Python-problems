n = [2,54,819,81,100]
l = len(n)
count = 0
for i in range(0, l):# checks in te list if each element is divisible by 27 or not and also tells if the number is divisible by 27 or not
    if n[i] % 27 ==0:
        n[i] - 1
        print("divisible by 27")
    else:
        print("not div by 27")
