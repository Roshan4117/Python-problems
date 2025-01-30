n = int(input("Enter the number of elements: "))

value= []

for a in range (n):
    integer = int(input("Enter the number:")) # adding values in the list
    value.append(integer)
    
print(value)

unique = []
for x in value:
    if x not in unique:# creating new list unique where repeated values are shown only once
            unique.append(x)
print(unique)

counts = []
for u in unique:
    count = 0
    for x in value:# counts how many time a single element is repeated
        if x == u:
            count += 1
    counts.append(count)
    
non_repeating_number = 0
max_count = 1
for i in range(len(counts)): # here if the count of sinlge element is equal to 1 then the output will be that number
    if max_count == counts[i] :
        non_repeating_number = unique[i]
        max_count = counts[i]
print(non_repeating_number)
    
