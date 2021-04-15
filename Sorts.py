def main_test():
    array = []
    num_elements = int(input("Enter number of elements: "))
    for i in range(0, num_elements):
        element = int(input())
        array.append(element)
    print(array)
    searchsort = int(input("Enter 1 for sort, 2 for search"))
    if searchsort == 1:
        sort = int(
            input("Enter 1 for bubble, 2 for insertion, 3 for selection: "))
        if sort == 1:
            bubble_sort(array)
        if sort == 2:
            insertion_sort(array)
        if sort == 3:
            selection_sort(array)
        print(array)
    else:
        search = int(
            input("Enter 1 for Binary, 2 for Linear. Note:Binary requires a sorted array"))
        target = int(input("Enter the target:"))
        found = 0
        if search == 1:
            found = binary_search(array, target)
        if search == 2:
            found = linear_search(array, target)
    if found == 1:
        print("Found")
    else:
        print("Not found")

def bubble_sort(array):
    last = len(array)+1
    swapped = 1
    while swapped == 1:
        swapped = 0
        index = 1
        if array[index] > array[index+1]:
            array[index], array[index+1] = array[index+1], array[index]
            swapped = 1
            if index < last:
                index = index+1
            last -= 1
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
    for index in range(len(array)-1):
        Min = index
        for unsorted in range(index+1, len(array)):
            if array[Min] < array[unsorted]:
                unsorted = Min
        array[index], array[unsorted] = array[unsorted], array[index]
    return array

def binary_search(array, target):
    low = 0
    high = len(array)-1
    while high >= low:
        mid = (high + low) // 2
        if target == array[mid]:
            return 1
        if target < array[mid]:
            high = mid-1
        if target > array[mid]:
            low = mid + 1
    return 0

def linear_search(array, target):
    for index in range(len(array)):
        if array[index] == target:
            return 1
    return 0

main_test()
