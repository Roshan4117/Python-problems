def bubble_sort(List):
    n = len(List)
    for i in range(n):
        for j in range(0, n-i-1):
            if List[j] > List[j+1]:
                List[j], List[j+1] = List[j+1], List[j]
    return List

numbers = [64, 34, 25, 12, 22, 11, 90]
print("Sorted list:", bubble_sort(numbers))

#This code is used for sorting the elements in the List without using the built in function. Here we are using the concept of Bubble sort to sort the elements in ascending order.
#This defined Function continues this process for each pass until the list is fully sorted. The outer loop controls the number of passes, while the inner loop performs the comparisons and swaps. After all elements are sorted, the function returns the sorted list.
#Bubble sort is a simple sorting algorithm that repeatedly compares and swaps adjacent elements in a list until the entire list is sorted.
