import time


# greedy algorithm chooses most valuable elements first
def knapsack_greedy(size, num, items):
    items.sort(key=lambda x: x[0], reverse=True)

    current_weight = 0
    current_value = 0
    result = []

    i = 0
    while current_weight < size and i <= num:
        if items[i][1] <= size - current_weight:
            result.append(items[i])
            current_weight += items[i][1]
            current_value += items[i][0]
        i += 1

    return current_value, result


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
val, res = knapsack_greedy(s, n, data)
end = time.time()
print("\nValue of items:", val)
print("Items:", res)
print("Greedy algorithm time:", end - start)
