s1 =input("Enter any string: ")
for i in range(len(s1)):
    for j in range(i+1, len(s1)+1):
        print(s1[i:j])
