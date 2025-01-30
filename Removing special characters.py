s = input("Enter the string:")
result = "" 
for str in s:
    if ( "A" <= str <= "Z") or ("a" <= str <= "z"): # removing special characters and white spaces in a given string
        result += str
print (result)