import time
from generating_list import *


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Helper function for Quick Sort
def partition(arr, left, right, piv_index):
    pivot = arr[piv_index]
    i = left
    j = right

    while True:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        else:
            return j


def quick_sort(arr, left, right, type_of_pivot):
    if left < right:
        pivot_index = left
        if type_of_pivot == "random":
            pivot_index = random.randint(left, right)
        partition_position = partition(arr, left, right, pivot_index)
        quick_sort(arr, left, partition_position, pivot_index)
        quick_sort(arr, partition_position + 1, right, pivot_index)
    return arr


# Helper function for Heap Sort
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


# Helper function for Merge Sort
def merge(left, right):
    arr = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    arr += left[i:]
    arr += right[j:]
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def shell_sort(arr):  # using Sedgewick sequence
    n = len(arr)
    gap = 1
    while gap < n // 3:
        gap = 3 * gap + 1

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 3

    return arr


def counting_sort(arr):
    max_value = max(arr)

    count = [0] * (max_value + 1)

    for i in arr:
        count[i] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    sorted_arr = [0] * len(arr)
    i = len(arr) - 1
    while i >= 0:
        sorted_arr[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    return sorted_arr


size = int(input("Enter number of elements: "))

data_generation = {"random": generate_random_list,
                   "ascending": generate_ascending_list,
                   "descending": generate_descending_list,
                   "constant": generate_constant_list,
                   "A-shaped": generate_a_shaped_list,
                   "custom": custom_list}

data_type = ""
curr_arr = []
while data_type not in data_generation:
    data_type = input("Enter the type of input sequence (random, ascending, descending, constant, A-shaped, custom): ")
    if data_type in data_generation:
        curr_arr = data_generation[data_type](size)
    else:
        print("Wrong choice.")

print("Available sorting algorithms:")
print("Naive sorting algorithms: Insertion Sort, Selection Sort, Bubble Sort")
print("Divide and conquer sorting algorithms: Quick Sort, Heap Sort, Merge Sort")
print("Other sorting algorithms: Shell Sort, Counting Sort\n")

sorting_algorithms = {"insertion sort": insertion_sort,
                      "selection sort": selection_sort,
                      "bubble sort": bubble_sort,
                      "quick sort": quick_sort,
                      "heap sort": heap_sort,
                      "merge sort": merge_sort,
                      "shell sort": shell_sort,
                      "counting sort": counting_sort}

chosen_algorithm = ""
while chosen_algorithm.lower() not in sorting_algorithms:
    chosen_algorithm = input("Choose one algorithm from options above: ")
    if chosen_algorithm.lower() in sorting_algorithms:
        if chosen_algorithm == "quick sort":
            pivot_type = ""
            while pivot_type not in ["left", "random"]:
                pivot_type = input("Choose a type of pivot (left, random): ")
            print("List before sorting:", curr_arr)
            start_time = time.time()
            sort_arr = sorting_algorithms[chosen_algorithm.lower()](curr_arr, 0, len(curr_arr) - 1, pivot_type)
            end_time = time.time()
        else:
            print("List before sorting:", curr_arr)
            start_time = time.time()
            sort_arr = sorting_algorithms[chosen_algorithm.lower()](curr_arr)
            end_time = time.time()
        print("List after sorting:", sort_arr)
        print("Sorting time:", end_time - start_time)
    else:
        print("Wrong choice.")
