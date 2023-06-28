import time


def knapsack_brute_force(size, num, items):
    fmax = 0
    result = []

    for i in range(1, 2 ** num - 1):
        binary_i = bin(i)[2:].zfill(num)

        current_weight = 0
        current_value = 0
        current_result = []

        for j in range(num):
            if binary_i[j] == '1':
                current_weight += items[j][1]
                if current_weight > size:
                    break
                current_value += items[j][0]
                current_result.append(items[j])

        if current_value > fmax:
            fmax = current_value
            result = current_result

    return fmax, result


with open("data.txt", 'r') as file:  # file name
    # each line represents an item (starting from the third line of the file)
    # the first column is the items' value and the second column is the items' weight
    lines = file.readlines()

s = int(lines[0].strip())  # first line represents knapsack's size
n = int(lines[1].strip())  # second line represents number of items

data = [[int(i.split()[0]), int(i.split()[1].strip())] for i in lines[2:]]

print("s:", s)  # knapsack's size
print("n:", n)  # number of items
print("Data (value, weight):", data)  # value, weight

start = time.time()
val, res = knapsack_brute_force(s, n, data)
end = time.time()
print("\nValue of items:", val)
print("Items:", res)
print("Brute force algorithm time:", end - start)
