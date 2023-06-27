import random


# Functions for generating different types of lists

def generate_random_list(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, n))
    return arr


def generate_ascending_list(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, n))
    arr.sort()
    return arr


def generate_descending_list(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, n))
    arr.sort(reverse=True)
    return arr


def generate_constant_list(n):
    arr = []
    x = random.randint(0, n)
    for i in range(n):
        arr.append(x)
    return arr


def generate_a_shaped_list(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, n))
    mid = n // 2
    arr_sorted = arr[:mid]
    arr_sorted_reverse = arr[mid:]
    arr_sorted.sort()
    arr_sorted_reverse.sort(reverse=True)
    a_shaped_arr = arr_sorted + arr_sorted_reverse
    return a_shaped_arr


def custom_list(n):
    arr = list(map(int, input("Enter {} elements in one line: ".format(n)).split()))
    return arr
