s = input("Enter the phrase:")
result = "" 
for str in s:
    if ( "A" <= str <= "Z") or ("a" <= str <= "z"):
        result += str
print (result)

for i in range( len(result) // 2):
    if result[i] != result[-(i + 1)]:
        print(False)
        break
    else:
        print(True)
        break
        
if True:
    print("palindrome")
else:
    print("not palindrome")