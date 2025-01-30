s = input("Enter the phrase:")
result = "" 
for char in s:
    if char != " ":
        result += char
print (result)

for i in range( len(result) // 2):
    if result[i] != result[-(i + 1)]:
        print(False)
    else:
        print(True)
        break
        
if True:
    print("palindrome")
else:
    print("not palindrome")