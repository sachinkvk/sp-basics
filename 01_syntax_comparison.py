"""
WEEK 1: Python Syntax Transfer for Swift Developers
Swift → Python Comparison

This file shows side-by-side Swift and Python equivalents.
Run this file to see the Python syntax in action.
"""

# ============================================================================
# 1. VARIABLES & TYPES
# ============================================================================

# Swift:
# let name: String = "Alice"
# var age: Int = 25
# let height: Double = 5.8

# Python (similar, but more flexible):
name: str = "Alice"
age: int = 25
height: float = 5.8

print("=== 1. VARIABLES & TYPES ===")
print(f"Name: {name}, Age: {age}, Height: {height}")


# ============================================================================
# 2. OPTIONALS / NULLABLE
# ============================================================================

# Swift:
# var email: String? = nil
# if let email = email { }

# Python (None replaces nil):
email: str | None = None  # or Optional[str]

print("\n=== 2. OPTIONALS ===")
if email is not None:
    print(f"Email: {email}")
else:
    print("Email is nil/None")


# ============================================================================
# 3. FUNCTIONS
# ============================================================================

# Swift:
# func greet(name: String, greeting: String = "Hello") -> String {
#     return "\(greeting), \(name)!"
# }

# Python:
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

print("\n=== 3. FUNCTIONS ===")
print(greet("Alice"))
print(greet("Bob", greeting="Hi"))


# ============================================================================
# 4. CLOSURES / LAMBDAS
# ============================================================================

# Swift:
# let numbers = [1, 2, 3, 4, 5]
# let doubled = numbers.map { $0 * 2 }

# Python:
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]  # List comprehension (preferred)
doubled_lambda = list(map(lambda x: x * 2, numbers))  # Or lambda

print("\n=== 4. CLOSURES/LAMBDAS ===")
print(f"Original: {numbers}")
print(f"Doubled: {doubled}")


# ============================================================================
# 5. FILTERING
# ============================================================================

# Swift:
# let evens = numbers.filter { $0 % 2 == 0 }

# Python:
evens = [x for x in numbers if x % 2 == 0]  # List comprehension
evens_filter = list(filter(lambda x: x % 2 == 0, numbers))  # Or filter

print("\n=== 5. FILTERING ===")
print(f"Even numbers: {evens}")


# ============================================================================
# 6. DICTIONARIES
# ============================================================================

# Swift:
# let person: [String: Any] = ["name": "Alice", "age": 25]
# person["name"] // "Alice"

# Python:
person: dict[str, str | int] = {"name": "Alice", "age": 25}
print("\n=== 6. DICTIONARIES ===")
print(f"Name: {person['name']}, Age: {person['age']}")

# Safe access (like Swift optional)
email_dict = person.get("email")  # Returns None if not found
print(f"Email: {email_dict}")


# ============================================================================
# 7. LOOPS
# ============================================================================

print("\n=== 7. LOOPS ===")

# Swift:
# for number in numbers {
#     print(number)
# }

# Python:
for number in numbers:
    print(number, end=" ")
print()

# With index (like enumerated in Swift):
# Swift: for (index, number) in numbers.enumerated()
for index, number in enumerate(numbers):
    print(f"[{index}]: {number}", end=" ")
print()


# ============================================================================
# 8. STRUCTS / CLASSES
# ============================================================================

# Swift:
# struct User {
#     let name: String
#     let age: Int
# }

# Python (class):
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def description(self) -> str:
        return f"{self.name} is {self.age} years old"

print("\n=== 8. CLASSES ===")
user = User("Alice", 25)
print(user.description())


# ============================================================================
# 9. ERROR HANDLING
# ============================================================================

# Swift:
# do {
#     try someFunction()
# } catch {
#     print(error)
# }

# Python:
def risky_operation(value: int) -> int:
    if value < 0:
        raise ValueError("Value must be positive")
    return value * 2

print("\n=== 9. ERROR HANDLING ===")
try:
    result = risky_operation(5)
    print(f"Result: {result}")
except ValueError as e:
    print(f"Error: {e}")


# ============================================================================
# 10. TYPE HINTS (BONUS - makes Python safer)
# ============================================================================

print("\n=== 10. TYPE HINTS ===")

def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return result."""
    return a + b

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# Python doesn't enforce types at runtime (unlike Swift)
# But type hints help with IDE autocomplete and static analysis

print("\n✅ All examples completed!")
