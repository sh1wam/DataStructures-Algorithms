def binarySearch(array, low, high, target):

    while low < high:

        mid = (low + high) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = int(input(f"Enter the element to be found in {array}: "))

    result = binarySearch(array, 0, len(array), target)

    if result != -1:
        print("Element is present at index", result)
    else:
        print("element not found")