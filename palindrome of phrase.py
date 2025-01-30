s = input("Enter the phrase:")
result = "" 
for str in s:
    if ( "A" <= str <= "Z") or ("a" <= str <= "z"):# here the empty spaces, special character are removed because the range is only between alphabets 
        result += str
print (result)

for i in range( len(result) // 2):
    if result[i] != result[-(i + 1)]:# here when the spaces and special characters are removed it checks if each elements in the first and last are equal or not 
        print(False)
        break
    else:
        print(True)
        break
        
if True:
    print("palindrome")# prints is palindrome or not
else:
    print("not palindrome")
