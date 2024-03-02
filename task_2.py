test_numbers = [0.1, 0.25, 0.5, 0.75, 1.0, 1.25,
                1.5, 1.75, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    count = 0

    while low <= high:
        mid = (low + high) // 2
        count += 1
        if arr[mid] == x:
            return (count, arr[mid])
        if arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1


print(binary_search(test_numbers, 1.75))
