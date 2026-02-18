# Week 1 Learning Guide: Python for Swift Developers

## 🎯 Overview

You have **4 practical exercises** designed to transfer your Swift knowledge to Python in just 3 hours.

**What you'll learn:**
- Python syntax that maps to Swift
- Building networking layers (like URLSession)
- Async/await patterns
- Data models and JSON handling

---

## 📚 Exercise Structure

### Exercise 1: Python Syntax Comparison (30 min)
**File:** `01_syntax_comparison.py`

**What you'll learn:**
- Variables and type hints (like Swift's typed vars)
- Functions with default parameters
- Collections (lists, dicts, tuples, sets)
- Control flow (if, for, while)
- Classes and methods
- Error handling (try/except)

**Key takeaway:** Python syntax is familiar - less ceremony than Swift, more flexibility

**Run it:**
```bash
python3 01_syntax_comparison.py
```

---

### Exercise 2: Build an API Client (45 min)
**File:** `02_exercise_api_client.py`

**What you'll learn:**
- Generic types (TypeVar) - like `<T>` in Swift
- Response handling (Result-like pattern)
- Building reusable API layers
- Error handling for network calls

**This mimics:**
```swift
class NetworkClient {
    func get<T>(_ endpoint: String) -> Result<T, Error>
}
```

**Exercises to complete:**
1. ✅ Understand the basic API client
2. TODO: Add `DELETE` method
3. TODO: Add authentication token support
4. TODO: Create a `User` model class
5. TODO: Parse JSON responses into User objects

**Run it:**
```bash
python3 02_exercise_api_client.py
```

---

### Exercise 3: Async/Await Patterns (60 min)
**File:** `03_exercise_async.py`

**What you'll learn:**
- `async def` and `await` (like Swift's async/await)
- `asyncio.gather()` for concurrent tasks (like `async let`)
- Timeout handling
- Error handling in async code

**This maps to:**
```swift
// Swift
async let result = fetchData()

// Python equivalent
tasks = [fetch_data(), fetch_data()]
results = await asyncio.gather(*tasks)
```

**Exercises to complete:**
1. ✅ Run concurrent requests
2. TODO: Handle partial failures with `return_exceptions=True`
3. TODO: Build a retry mechanism
4. TODO: Create an async context manager

**Run it:**
```bash
python3 03_exercise_async.py
```

---

### Exercise 4: Data Models (45 min)
**File:** `04_exercise_data_models.py`

**What you'll learn:**
- Dataclasses (lightweight, Swift struct-like)
- Pydantic (with validation, like Codable)
- JSON serialization/deserialization
- Validation rules

**This replaces Codable:**
```swift
// Swift
struct User: Codable {
    let id: Int
    let name: String
}

// Python
@dataclass
class User:
    id: int
    name: str
```

**Exercises to complete:**
1. ✅ Serialize/deserialize with dataclasses
2. TODO: Create a `Student` model with GPA validation
3. TODO: Create a `Course` model with list of students
4. TODO: Use Pydantic for validation

**Run it:**
```bash
python3 04_exercise_data_models.py
```

---

## ⏱️ Suggested 3-Day Schedule

### Day 1 (90 minutes)
```
09:00 - 09:30  Exercise 1: Read & run syntax comparison
09:30 - 10:15  Exercise 2: Build basic API client
10:15 - 10:30  Break
```

### Day 2 (90 minutes)
```
09:00 - 09:30  Exercise 2: Complete TODO 2-3 (auth, User model)
09:30 - 10:30  Exercise 3: Run async examples, understand patterns
10:30 - 10:45  Break
```

### Day 3 (90 minutes)
```
09:00 - 09:30  Exercise 3: Complete TODO 2-4 (partial failures, retry, context manager)
09:30 - 10:30  Exercise 4: Dataclasses + Pydantic, complete TODOs
10:30 - 11:00  Review and experimentation
```

---

## 🚀 Getting Started

### 1. Check your environment
```bash
python3 check_setup.py
```

You should see:
```
✅ Python version: 3.14.2
✅ Standard library checks: PASS
✅ Optional packages: INSTALLED
```

### 2. Start with Exercise 1
```bash
python3 01_syntax_comparison.py
```

You'll see output like:
```
=== 1. VARIABLES & TYPES ===
Name: Alice, Age: 25, Height: 5.8
...
✅ All examples completed!
```

### 3. Work through each exercise in order
Read the code → Run it → Complete the TODO exercises

### 4. Experiment!
Modify the examples. Try breaking them. Fix the errors.

---

## 🔑 Swift ↔ Python Cheat Sheet

| Concept | Swift | Python |
|---------|-------|--------|
| **Variables** | `var x = 5` | `x: int = 5` |
| **Constants** | `let x = 5` | `x: int = 5` (convention) |
| **Type Hints** | Automatic | `x: int` (optional) |
| **Functions** | `func add(_ a: Int, _ b: Int) -> Int` | `def add(a: int, b: int) -> int:` |
| **Default Params** | `func greet(_ name: String = "Alice")` | `def greet(name: str = "Alice"):` |
| **Optionals** | `String?` / `nil` | `Optional[str]` / `None` |
| **Closures** | `{ $0 * 2 }` | `lambda x: x * 2` |
| **Arrays** | `[1, 2, 3]` | `[1, 2, 3]` |
| **Dictionaries** | `["key": "value"]` | `{"key": "value"}` |
| **Classes** | `class User: Codable` | `class User:` |
| **Structs** | `struct User` | `@dataclass class User:` |
| **Async** | `async let result = fetch()` | `result = await fetch()` |
| **Errors** | `do/try/catch` | `try/except` |
| **Generics** | `<T>` | `TypeVar('T')` |

---

## 📖 After Week 1

You'll be ready for:
- **Week 2:** Real API integration with `requests` library
- **Week 3:** Introduction to LLMs and Claude API
- **Week 4:** Building your first agent

---

## ❓ Tips for Success

**Do:**
- ✅ Run every file and see the output
- ✅ Modify examples and experiment
- ✅ Complete the TODO exercises
- ✅ Take notes on what's different from Swift
- ✅ Ask questions in VS Code's terminal

**Don't:**
- ❌ Skip exercises thinking you understand
- ❌ Copy-paste without reading
- ❌ Get frustrated with errors (they're learning!)
- ❌ Try to memorize - focus on understanding

---

## 🛠️ Tools You'll Use

- **Python 3.14.2** - Already installed ✅
- **VS Code** - Your editor
- **Terminal** - For running scripts
- **No frameworks needed** - Just Python stdlib for Week 1

---

## 💡 Quick Help

**Run a specific exercise:**
```bash
python3 01_syntax_comparison.py
```

**Run all exercises:**
```bash
for f in 0*.py; do echo "Running $f..."; python3 "$f"; echo ""; done
```

**Check Python version:**
```bash
python3 --version
```

**View file contents:**
```bash
cat 01_syntax_comparison.py
```

---

## 📋 Checklist

- [ ] Run `check_setup.py` - verify environment
- [ ] Complete Exercise 1 - Syntax comparison
- [ ] Complete Exercise 2 - API client
- [ ] Complete Exercise 3 - Async/await
- [ ] Complete Exercise 4 - Data models
- [ ] Experiment with modifications
- [ ] Ready for Week 2!

---

**Next Action:** Run `python3 check_setup.py` then start Exercise 1! 🎉
