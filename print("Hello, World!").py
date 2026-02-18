import random

print("Hello, World!")

def add(a, b):
    return a + b

print(add(5, 3))

def sort_array(arr):
    return sorted(arr)

random_array = [random.randint(1, 100) for _ in range(10)]
print(sort_array(random_array))
# Demonstrate string formatting and loops
for i in range(3):
    print(f"Iteration {i + 1}")

# Dictionary example
person = {"name": "Alice", "age": 30}
print(person)

# List operations
numbers = [1, 2, 3, 4, 5]
print(f"Sum: {sum(numbers)}, Average: {sum(numbers) / len(numbers)}")