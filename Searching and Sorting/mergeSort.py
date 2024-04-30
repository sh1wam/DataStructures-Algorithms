# --------MERGE-SORT PROGRAM ------

def merge(arr1, arr2):
    i = 0
    j = 0
    result = []

    while (i < len(arr1) and j < len(arr2)):
        if arr2[j] > arr1[i]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j+=1

    while (i < len(arr1)):
        result.append(arr1[i])
        i += 1

    while (j < len(arr2)):
        result.append(arr2[j])
        j += 1
    
    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)

# DRIVER-CODE
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("given array is: ", *arr)
    arr = mergeSort(arr)
    print("sorted array is: ", *arr)
    