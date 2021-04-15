def main_test():
    array = []
    num_elements = int(input("Enter number of elements: "))
    for i in range(0, num_elements):
        element = int(input())
        array.append(element)
    print(array)
    sort = int(input("Enter 1 for bubble, 2 for insertion, 3 for selection: "))
    if sort == 1:
        bubble_sort(array)
    if sort == 2:
        insertion_sort(array)
    if sort == 3:
        selection_sort(array)
    print(array)

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

main_test()
