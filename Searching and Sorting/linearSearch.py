def linearSearch(array, target):

    for i in range(0, len(array)):
        if (array[i] == target):
            return i
    return -1

if __name__ == "__main__":

    array = [10, 50, 30, 70, 80, 20, 90, 40]
    target = int(input(f"Enter the number to be found in {array}: "))

    result = linearSearch(array, target)

    if (result == -1):
        print("element not present int the list")
    else:
        print(f"Element present at index {result}")