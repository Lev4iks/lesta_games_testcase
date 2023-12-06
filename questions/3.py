def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = [n for n in arr if n < pivot]
    middle = [n for n in arr if n == pivot]
    right = [n for n in arr if n > pivot]
    return quick_sort(left) + middle + quick_sort(right)
