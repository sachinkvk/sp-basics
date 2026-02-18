"""
QUICK START: Run these 5 exercises in order

Week 1 Learning Path
"""

def exercise_1_syntax():
    """
    Exercise 1: Python Syntax Transfer (30 min)
    Run: python3 01_syntax_comparison.py
    
    Learn:
    - Variables and type hints
    - Functions and default parameters
    - Lists, dicts, tuples
    - Control flow (if, for, while)
    - Classes and methods
    - Error handling (try/except)
    """
    print("📘 Exercise 1: Python Syntax Comparison")
    print("   File: 01_syntax_comparison.py")
    print("   Time: 30 minutes")
    print("   Topics: Variables, Functions, Collections, Classes")


def exercise_2_api_client():
    """
    Exercise 2: Build API Client (45 min)
    Run: python3 02_exercise_api_client.py
    
    Learn:
    - Generic types (TypeVar)
    - Response handling (like Result in Swift)
    - Error handling
    - HTTP methods (GET, POST, DELETE)
    
    Tasks:
    1. Add DELETE method
    2. Add authentication token
    3. Create User model
    4. Parse JSON responses
    """
    print("\n📘 Exercise 2: API Client (Swift-style)")
    print("   File: 02_exercise_api_client.py")
    print("   Time: 45 minutes")
    print("   Topics: Classes, Generics, Error Handling")
    print("   Tasks: Add DELETE, auth, User model, JSON parsing")


def exercise_3_async():
    """
    Exercise 3: Async/Await (60 min)
    Run: python3 03_exercise_async.py
    
    Learn:
    - async/await (like Swift's async/await)
    - asyncio.gather() for concurrent tasks
    - Timeout handling
    - Task management
    
    Tasks:
    1. Create sequential fetch (5 users)
    2. Handle partial failures
    3. Add retry mechanism
    4. Create async context manager
    """
    print("\n📘 Exercise 3: Async/Await")
    print("   File: 03_exercise_async.py")
    print("   Time: 60 minutes")
    print("   Topics: Async, Concurrency, Error Handling")
    print("   Tasks: Sequential, Partial failures, Retry, Context manager")


def exercise_4_data_models():
    """
    Exercise 4: Data Models (45 min)
    Run: python3 04_exercise_data_models.py
    
    Learn:
    - Dataclasses (lightweight)
    - Pydantic (with validation)
    - JSON serialization/deserialization
    - Nested models
    - Validation
    
    Tasks:
    1. Create Student model
    2. Create Course model with students
    3. Serialize to JSON
    4. Add Pydantic validation
    """
    print("\n📘 Exercise 4: Data Models (Codable)")
    print("   File: 04_exercise_data_models.py")
    print("   Time: 45 minutes")
    print("   Topics: Dataclasses, Pydantic, JSON, Validation")
    print("   Tasks: Student/Course models, serialization, validation")


def print_schedule():
    """Print the complete Week 1 schedule"""
    print("\n" + "="*60)
    print("WEEK 1: PYTHON SYNTAX TRANSFER FOR SWIFT DEVELOPERS")
    print("="*60)
    
    exercise_1_syntax()
    exercise_2_api_client()
    exercise_3_async()
    exercise_4_data_models()
    
    print("\n" + "="*60)
    print("TOTAL TIME: ~3 hours")
    print("="*60)
    print("""
DAILY SCHEDULE (Suggested):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Day 1 (90 min):
  ✅ Exercise 1: Syntax Comparison (30 min)
     Read the file and run it. Try modifying examples.
  
  ✅ Exercise 2: API Client Part 1 (45 min)
     Build the basic client, understand the structure.
     Try to complete TODO #1 (DELETE method).

Day 2 (90 min):
  ✅ Exercise 2: API Client Part 2 (30 min)
     Complete TODO #2-4 (auth, User model, parsing)
  
  ✅ Exercise 3: Async/Await Part 1 (60 min)
     Run the examples, understand async/await syntax.

Day 3 (90 min):
  ✅ Exercise 3: Async Part 2 (30 min)
     Complete 2-3 of the async TODOs.
  
  ✅ Exercise 4: Data Models (60 min)
     Try both dataclasses and Pydantic.
     Complete the Student/Course exercise.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NEXT STEPS AFTER WEEK 1:
1. Install requests library: pip3 install requests
2. Build a real API client using JSONPlaceholder API
3. Start Week 2: Introduction to LLMs
""")


def installation_guide():
    """Print what to install"""
    print("\n" + "="*60)
    print("REQUIRED INSTALLATIONS (Optional - for later exercises)")
    print("="*60)
    print("""
For Week 1 (Python Basics):
  ✅ Python 3.10+ (already installed: 3.14.2)
  ✅ VS Code (should have it)
  
For Week 2 (APIs):
  🔄 pip3 install requests
  🔄 pip3 install pydantic
  
For Week 3 (LLMs):
  🔄 pip3 install anthropic
  🔄 pip3 install python-dotenv

Commands to run:
  pip3 install --upgrade pip
  pip3 install requests pydantic python-dotenv anthropic
""")


if __name__ == "__main__":
    print_schedule()
    installation_guide()
    print("\n" + "="*60)
    print("🚀 GET STARTED")
    print("="*60)
    print("""
Next action:
1. Open: 01_syntax_comparison.py
2. Read through the examples
3. Run: python3 01_syntax_comparison.py
4. Modify examples and experiment

Questions?
- Check the TODO comments in each file
- Run the exercises and see the output
- Modify the code and test your changes
""")
