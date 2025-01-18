def bubble_sort(List):
    n = len(List)
    for i in range(n):
        for j in range(0, n-i-1):
            if List[j] > List[j+1]:
                List[j], List[j+1] = List[j+1], List[j]
    return List

numbers = [64, 34, 25, 12, 22, 11, 90]
print("Sorted list:", bubble_sort(numbers))
