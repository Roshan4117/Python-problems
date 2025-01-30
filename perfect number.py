n = int(input("Enter the number: "))

factors = []
sum = 0
for i in range(1,n+1):
    if i < n:
        if n % i == 0:
            factors.append(i)
            sum += i
            print(factors)
if sum == n:
    print(True)
else:
    print(False)
            
     
