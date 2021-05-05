def main_test():
    array = []  # creates a list with intrinsic documentation indicating it is the array
    # User inputs the number of elements
    num_elements = int(input("Enter number of elements: "))
    # A for loop is used, repeating as many times as there are elements
    for i in range(0, num_elements):
        element = int(input("Enter element: "))  # takes input of the element
        array.append(element)  # Appends the element to the array
    print(array)  # Shows the user the array before processing
    # inputs the variable used to decide which type of algorithm to use
    searchsort = int(input("Enter 1 for sort, 2 for search"))
    if searchsort == 1:  # checks if the user selected search
        # inputs the variable for type of search
        sort = int(
            input("Enter 1 for bubble, 2 for insertion, 3 for selection: "))
        if sort == 1:  # checks if bubble is selected
            bubble_sort(array)
        if sort == 2:  # checks if insertion is selected
            insertion_sort(array)
        if sort == 3:  # checks if selection is selected
            selection_sort(array)
        print("The sorted array is: ", array)  # prints the sorted array
    else:
        # inputs the type of search
        search = int(
            input("Enter 1 for Binary, 2 for Linear. Note:Binary requires a sorted array"))
        target = int(input("Enter the target:"))  # inputs the target
        found = False
        if search == 1:
            binary_search(array, target)
        if search == 2:
            linear_search(array, target)
        if found == True:
            print("Found")
        else:
            print("Not found")


def bubble_sort(array):
    for index in range(len(array)):
        for index in range(len(array)-1):
            if array[index] > array[index+1]:
                array[index], array[index+1] = array[index+1], array[index]
    return array


def insertion_sort(array):
    for posofnext in range(1, len(array)):
        Next = array[posofnext]
        current = posofnext-1
        while current >= 0 and Next < array[current]:
            array[current + 1] = array[current]
            current -= 1
        array[current + 1] = Next
    return array


def selection_sort(array):
    for index in range(len(array)):
        Min = index
        for unsorted in range(index+1, len(array)):
            if array[Min] > array[unsorted]:
                Min = unsorted
        array[Min], array[index] = array[index], array[Min]
    return array


def binary_search(array, target):
    global found
    low = 0
    high = len(array)-1
    while high >= low:
        mid = (high + low) // 2
        if target == array[mid]:
            found = True
        if target < array[mid]:
            high = mid-1
        if target > array[mid]:
            low = mid + 1
    return


def linear_search(array, target):
    global found
    for index in range(len(array)):
        if array[index] == target:
            found = True
            return found
    return


main_test()
