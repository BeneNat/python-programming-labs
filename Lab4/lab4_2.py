import random

numbers = [random.randint(0, 100) for _ in range(50)]
print("Drawn numbers:")
print(numbers)

def sort_desc(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    return arr

sorted_numbers = sort_desc(numbers)

print("\nSorted (desc) (my function):")
print(sorted_numbers)

builtin_sorted = sorted(numbers, reverse=True)

print("\nSorted (desc) (built-in function):")
print(builtin_sorted)

print("\nAre they same?", sorted_numbers == builtin_sorted)