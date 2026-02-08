#lists
l = [1,2,3,4,5]
print(l)

# =========================
# Day 4 – Python Lists
# =========================

# 1. Creating a list
numbers = [1, 2, 3, 4, 5]
print(numbers)

# 2. Accessing elements
print(numbers[0])     # first element
print(numbers[-1])    # last element

# 3. Modifying list elements (lists are mutable)
numbers[2] = 99
print(numbers)

# 4. List methods
numbers.append(6)     # add element at end
print(numbers)

numbers.insert(1, 10) # insert at index
print(numbers)

numbers.remove(99)    # remove by value
print(numbers)

popped = numbers.pop() # remove last element
print("Popped:", popped)
print(numbers)

# 5. List length
print("Length:", len(numbers))

# 6. Looping through a list
for num in numbers:
    print(num)

# 7. List slicing
print(numbers[1:4])
print(numbers[:3])
print(numbers[::2])

# 8. List with mixed data types
mixed = [1, "Shikhar", 3.14, True]
print(mixed)

# 9. Nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix)
print(matrix[1][2])

# 10. Copying lists
a = [1, 2, 3]
b = a.copy()
b.append(4)
print("a:", a)
print("b:", b)
