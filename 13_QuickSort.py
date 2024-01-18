def quicksort(arr, low, high):
    if low < high:
        # partition the array
        pivot_index = partition(arr, low, high)

        # sort the left and right subarrays recursively
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    # choose the rightmost element as the pivot
    pivot = arr[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    for j in range(low, high):
        # if element is smaller than pivot, swap it with a larger element
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # swap the pivot element with the greater element pointed to by i
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # return the position from where partition is done
    return i + 1



data = [36, 12, 72, 4, 59, 93, 33, 47, 13, 68, 83, 12,  74]
print("Data:\t", data)
quicksort(data, 0, 12)
print("Sorted:\t", data)