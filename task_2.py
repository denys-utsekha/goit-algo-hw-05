test_numbers = [0.1, 0.25, 0.5, 0.75, 1.0, 1.25,
                1.5, 1.75, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]


def binary_search_with_upper_bound(arr, x):
    low = 0
    high = len(arr) - 1
    count = 0
    upper_bound = arr[-1]

    while low <= high:
        mid = (low + high) // 2
        count += 1

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1
        else:
            return count, arr[mid]

    return count, upper_bound


print(binary_search_with_upper_bound(test_numbers, 0.26))
