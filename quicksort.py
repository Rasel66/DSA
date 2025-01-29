def quicksort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    pivot = arr[n // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

arr = [2, 5, 4, 8, 1, 3, 10, 7]
sorted_array = quicksort(arr)
print(sorted_array)