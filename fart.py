def main_test():
    array = []
    n = int(input("Enter number of elements: "))
    for i in range(0, n):
        ele = int(input())
        array.append(ele)
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
            swap(array, index, index+1)
            swapped = 1
            if index < last:
                index = index+1
            last -= 1
    return array


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]
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
    B = 1


main_test()
