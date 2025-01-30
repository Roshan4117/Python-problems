n = int(input("Enter the number: "))

factors = []
sum = 0
for i in range(1,n+1):# here we are appending the number to factors where each factor is found and then they are added together which results as the same number
    if i < n:
        if n % i == 0:
            factors.append(i)
            sum += i # here if we give 28 as the number.. the factors when added will give same 28 number 
            print(factors)
if sum == n:
    print(True)
else:
    print(False)
            
     
