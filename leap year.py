year = int (input ("Enter the year:"))

if year % 4 == 0:
    print(True)
    if year % 100 == 0:
        print(False)
        if year % 400 == 0:
            print(True)
if True:
    print("leap year")
else:
    print("Not a leap year ")    
    
    

optimized_year = int(input("Enter the year"))

if optimized_year % 4 == 0 and (optimized_year % 100 != 0 or optimized_year % 400 == 0):
    print("leap year")
else:
    print("Not a leap year")