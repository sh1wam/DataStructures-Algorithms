def binarySearch(array, low, high, target):
    while low <= high:

        mid = low + (high - low) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return False

if __name__ == '__main__':
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target = int(input(f"Enter the number to find in {arr} :"))
    result = binarySearch(arr, 0, len(arr)-1, target)

    if(result):
        print(f"the number {target} was found at index {result}")
    else:
        print("not found")