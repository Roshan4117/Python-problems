def dup(x):
    unique = []
    for item in x:
        if item not in unique:
            unique.append(item)
    
    counts =[]
    for u in unique:
        count = 0
        for item in x:
            if item == u:
                count += 1
        counts.append(count)
        
    max_number = 0
    max_counts = 0
    for i in range(len(counts)):
        if max_counts < counts[i] or (max_counts == counts[i] and max_number < unique[i]):
            max_number = unique[i]
            max_counts = counts[i]
    return max_counts, max_number


x = [1,1,2,2,2,3,4,5,6,6,6,6]
print("",dup(x))