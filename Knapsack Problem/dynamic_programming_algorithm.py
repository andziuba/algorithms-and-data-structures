import time


def knapsack_dynamic_programming(size, num, items):
    matrix = [[0] * (size + 1) for _ in range(num + 1)]

    for i in range(num + 1):
        value = items[i - 1][0]
        weight = items[i - 1][1]

        for j in range(size + 1):
            if i == 0 or j == 0:
                continue
            elif weight <= j:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i - 1][j - weight] + value)
            else:
                matrix[i][j] = matrix[i - 1][j]

    result = []
    j = size
    i = num
    while j > 0 and i > 0:
        if matrix[i][j] > matrix[i - 1][j]:
            result.append(items[i - 1])
            i -= 1
            j -= items[i - 1][1]
        else:
            i -= 1

    return matrix[num][size], result


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
val, res = knapsack_dynamic_programming(s, n, data)
end = time.time()
print("\nValue of items:", val)
print("Items:", res)
print("Dynamic programming algorithm time:", end - start)
