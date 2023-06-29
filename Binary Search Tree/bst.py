"""
The program generates or creates from given nodes a Binary Search Tree (BST) and performs the following operations on it:
* reading the height of a BST
* searching for the minimum value and printing the path of the search
* searching for the maximum value and printing the path of the search
* eleting node/nodes of a BST
* printing all nodes of a BST in-order, pre-order or post-order
* deleting all nodes of a BST (using post-order)
* balancing a BST by rotation using the Day–Stout–Warren algorithm (DSW)
"""
import math


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.rheight = 0
        self.lheight = 0

    def insert(self, value):
        if not self:
            return Node(value)
        if value < self.value:
            self.left = Node.insert(self.left, value)
        elif value > self.value:
            self.right = Node.insert(self.right, value)
        return self

    def delete(self, value):
        if not self:
            return self
        if value < self.value:
            self.left = Node.delete(self.left, value)
            return self
        if value > self.value:
            self.right = Node.delete(self.right, value)
            return self
        if not self.right:
            return self.left
        if not self.left:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.value = min_larger_node.value
        self.right = self.right.delete(min_larger_node.value)
        return self

    # left child, parent, right child
    def in_order(self, values):
        if self is not None and self.left is not None:
            Node.in_order(self.left, values)
        if self is not None and self.value is not None:
            values.append(self.value)
        if self is not None and self.right is not None:
            Node.in_order(self.right, values)
        return values

    # parent, left child, right child
    def pre_order(self, values):
        if self is not None and self.value is not None:
            values.append(self.value)
        if self is not None and self.left is not None:
            Node.pre_order(self.left, values)
        if self is not None and self.right is not None:
            Node.pre_order(self.right, values)
        return values

    # left child, right child, parent
    def post_order(self, values):
        if self is not None and self.left is not None:
            Node.post_order(self.left, values)
        if self is not None and self.right is not None:
            Node.post_order(self.right, values)
        if self is not None and self.value is not None:
            values.append(self.value)
        return values

    def height(self):
        if self.value is None:
            return 0
        else:
            if self.left is not None:
                self.lheight = Node.height(self.left)
            if self.right is not None:
                self.rheight = Node.height(self.right)
            return 1 + max(self.lheight, self.rheight)

    def search_for_max(self):
        current = self
        searched = [current.value]
        while current.right is not None:
            current = current.right
            searched.append(current.value)
        return current.value, searched

    def search_for_min(self):
        current = self
        searched = [current.value]
        while current.left is not None:
            current = current.left
            searched.append(current.value)
        return current.value, searched


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = Node.insert(self.root, value)

    def delete(self, value):
        self.root = Node.delete(self.root, value)

    def pre_order(self, values=None):
        return Node.pre_order(self.root, values)

    def in_order(self, values=None):
        return Node.in_order(self.root, values)

    def post_order(self, values):
        return Node.post_order(self.root, values)

    def search_for_max(self):
        return Node.search_for_max(self.root)

    def search_for_min(self):
        return Node.search_for_min(self.root)

    def height(self):
        return Node.height(self.root)

    def dsw(self):
        if self.root is not None:
            self.create_vine()
            self.balance()

    def create_vine(self):
        grandparent = None
        parent = self.root
        left_child = None

        while parent is not None:
            left_child = parent.left
            if left_child is not None:
                grandparent = self.rotate_right(grandparent, parent, left_child)
                parent = left_child
            else:
                grandparent = parent
                parent = parent.right

    def rotate_right(self, grandparent, parent, left_child):
        if grandparent is not None:
            grandparent.right = left_child
        else:
            self.root = left_child

        parent.left = left_child.right
        left_child.right = parent
        return grandparent

    def balance(self):
        global n
        m = pow(2, math.floor(math.log2(n + 1))) - 1
        self.make_rotations(n - m)

        while m > 1:
            m //= 2
            self.make_rotations(m)

    def make_rotations(self, bound):
        grandparent = None
        parent = self.root
        child = self.root.right
        while bound > 0:
            if child is not None:
                self.rotate_left(grandparent, parent, child)
                grandparent = child
                parent = grandparent.right
                child = parent.right
            else:
                break
            bound -= 1

    def rotate_left(self, grandparent, parent, right_child):
        if grandparent is not None:
            grandparent.right = right_child
        else:
            self.root = right_child

        parent.right = right_child.left
        right_child.left = parent


def check_for_duplicates(lst):
    new_lst = []
    global n
    n = 0
    for element in lst:
        if element not in new_lst:
            new_lst.append(element)
            n += 1
    return new_lst, n


data_type = input("Do you want to generate ascending sequence - will create a vine (a) or enter elements of sequence (b): ")
n = int(input("Enter a number of elements: "))

sequence = []

if data_type == "a":
    for i in range(1, n + 1):
        sequence.append(i)
elif data_type == "b":
    print("Enter " + str(n) + " numbers in one line:")
    sequence = [int(x) for x in input().split()]
    while len(sequence) != n:
        print("Enter again " + str(n) + " in one line:")
        sequence = [int(x) for x in input().split()]
    sequence, n = check_for_duplicates(sequence)
else:
    print("Wrong choice.")

print("Sequence:", sequence)

# Creating a BST
tree = BST()
for i in sequence:
    tree.insert(i)

print("Binary search tree has been made.\n")


# Functions for chosen operations

def read_height():
    print(tree.height())
    return


def read_minimum():
    min_value, searched_min = tree.search_for_min()
    print("Wartosc minimalna:", min_value)
    print("Sciezka poszukiwania wartosci minimalnej:", searched_min)
    return


def read_maximum():
    max_value, searched_max = tree.search_for_max()
    print("Wartosc maksymalna:", max_value)
    print("Sciezka poszukiwania wartosci maksymalnej:", searched_max)
    return


def delete_elements():
    values_to_delete = [int(x) for x in input("Podaj wartosci do usuniecia (w jednej linii): ").split()]
    for el in values_to_delete:
        tree.delete(el)
    return


def print_in_order():
    in_order_arr = []
    print("In-order:")
    print(tree.in_order(in_order_arr))
    return


def print_pre_order():
    pre_order_arr = []
    print("Pre-order:")
    print(tree.pre_order(pre_order_arr))
    return


def print_post_order():
    post_order_arr = []
    print("Post-order:")
    print(tree.post_order(post_order_arr))
    return


def delete_whole_tree():
    post_order_arr = []
    tree.post_order(post_order_arr)
    for el in post_order_arr:
        tree.delete(el)
    return


def rotation_dsw():
    tree.dsw()
    return


def close_or_continue():
    x = input("\nChoose the next operation (a) or close the program (b): ")
    if x == "a":
        return True
    elif x == "b":
        return False
    else:
        print("Wrong choice")
        return close_or_continue()


print("Available operations: \n(1) Reading the height of a BST")
print("(2) Searching for the minimum value and printing the path of the search")
print("(3) Searching for the maximum value and printing the path of the search")
print("(4) Deleting node/nodes of a BST")
print("(5) Printing all nodes of a BST (in-order)")
print("(6) Printing all nodes of a BST (pre-order)")
print("(7) Printing all nodes of a BST (post-order)")
print("(8) Deleting all nodes of a BST (using post-order)")
print("(9) Balancing a BST by rotation (Day–Stout–Warren (DSW) algorithm)")

operations = {"1": read_height,
              "2": read_minimum,
              "3": read_maximum,
              "4": delete_elements,
              "5": print_in_order,
              "6": print_pre_order,
              "7": print_post_order,
              "8": delete_whole_tree,
              "9": rotation_dsw}

tag = True
while tag:
    operation = input("Choose a number of operation: ")
    if operation in operations:
        operations[operation]()
    else:
        print("Wrong choice")
    tag = close_or_continue()
