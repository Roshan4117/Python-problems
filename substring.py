s1 =input("Enter any string: ")
for i in range(len(s1)):
    for j in range(i+1, len(s1)+1): # a small program that has a substring and prints the substring by iterating each staring index to ending indices
        print(s1[i:j])
