# Function to find the partition position
def partition(array, low, high):

    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low-1

    # Traverse through all elements
    # compare each element with pivot
    for j in range (low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is founnd
            # swap is with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
    
    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1

# Function to perform quickSort
def quickSort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pivot = partition(array, low, high)

        # Recursive call on the left of the pivot
        quickSort(array, low, pivot-1)

        # Recursive call on the right of the pivot
        quickSort(array, pivot+1, high)

# Driver-Code
if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    N = len(array)

    quickSort(array, 0, N-1)

    print("Sorted Array: ")
    for x in array:
        print(x, end=" ")