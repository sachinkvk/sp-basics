"""
EXERCISE 2: Async/Await (Like Task in Swift Concurrency)

Swift → Python async/await translation
"""

import asyncio
from typing import Optional


# ============================================================================
# SIMPLE ASYNC EXAMPLE
# ============================================================================

# Swift:
# func fetchData() async -> String {
#     let data = await URLSession.shared.data(from: url)
#     return String(data: data.0, encoding: .utf8) ?? ""
# }

# Python:
async def fetch_data(delay: float = 1) -> str:
    """Simulate async network call"""
    print("🔄 Fetching data...")
    await asyncio.sleep(delay)  # Simulate network delay
    print("✅ Data fetched!")
    return "User data from API"


# ============================================================================
# CALLING ASYNC FUNCTIONS
# ============================================================================

# Swift:
# Task {
#     let data = await fetchData()
#     print(data)
# }

# Python:
async def main():
    """Run async code"""
    result = await fetch_data(delay=2)
    print(f"Result: {result}")


# ============================================================================
# MULTIPLE CONCURRENT REQUESTS (Like Task.sleep in Swift)
# ============================================================================

async def fetch_user(user_id: int) -> dict:
    """Fetch a single user"""
    await asyncio.sleep(1)  # Simulate API call
    return {"id": user_id, "name": f"User{user_id}"}


async def fetch_all_users(user_ids: list[int]) -> list[dict]:
    """
    Fetch multiple users concurrently
    Swift equivalent: async let user1 = fetchUser(1); async let user2 = fetchUser(2); etc
    """
    # Create all tasks concurrently
    tasks = [fetch_user(uid) for uid in user_ids]
    
    # Wait for all to complete
    results = await asyncio.gather(*tasks)
    return results


# ============================================================================
# TIMEOUT HANDLING
# ============================================================================

async def fetch_with_timeout(delay: float = 5, timeout: float = 2) -> Optional[str]:
    """
    Fetch with timeout
    Swift: try? await withThrowingTaskGroup
    """
    try:
        result = await asyncio.wait_for(
            fetch_data(delay),
            timeout=timeout
        )
        return result
    except asyncio.TimeoutError:
        return None


# ============================================================================
# RUNNING EXAMPLES
# ============================================================================

async def run_examples():
    print("=== Example 1: Simple Async ===")
    result = await fetch_data(delay=1)
    print(f"Got: {result}\n")
    
    print("=== Example 2: Concurrent Requests ===")
    users = await fetch_all_users([1, 2, 3])
    for user in users:
        print(f"  {user}")
    print()
    
    print("=== Example 3: Timeout ===")
    result = await fetch_with_timeout(delay=1, timeout=2)
    print(f"Result: {result}")
    
    result = await fetch_with_timeout(delay=5, timeout=1)
    print(f"Result (timeout): {result}")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    # Run async code
    # In Swift: just use async/await
    # In Python: use asyncio.run()
    asyncio.run(run_examples())


# ============================================================================
# EXERCISES
# ============================================================================

"""
TODO - Complete these:

1. Create an async function that fetches 5 users sequentially (not concurrently)
   - Should take ~5 seconds total
   
2. Modify fetch_all_users to handle partial failures
   - If one user fails, others should still complete
   - Use asyncio.gather(return_exceptions=True)

3. Create a retry mechanism
   - def async_retry(func, max_retries=3)
   - Retry if the first attempt fails

4. Build an async context manager
   - async with NetworkSession() as session:
   -     data = await session.fetch(url)

HINT: In Python, we use:
- async def for async functions (like async in Swift)
- await to wait for results (like await in Swift)  
- asyncio.gather() to run concurrent tasks (like async let in Swift)
"""
