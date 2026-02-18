"""
EXERCISE 1: Swift Developer - Python Practice
Networking Layer (Like URLSession in Swift)

This mimics how you build networking layers in iOS.
"""

from typing import Optional, TypeVar, Generic
import json

# ============================================================================
# EXERCISE: Build a Generic API Client (Swift-style)
# ============================================================================

T = TypeVar('T')  # Generic type (like <T> in Swift)


class APIResponse(Generic[T]):
    """Generic response wrapper (similar to Result<T, Error> in Swift)"""
    
    def __init__(self, data: Optional[T] = None, error: Optional[str] = None):
        self.data = data
        self.error = error
    
    def is_success(self) -> bool:
        return self.error is None


class APIClient:
    """
    Simple API Client
    Similar to your URLSession + custom networking layer in Swift
    """
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}
    
    def build_url(self, endpoint: str) -> str:
        """Build full URL"""
        return f"{self.base_url}/{endpoint}"
    
    def get(self, endpoint: str) -> APIResponse[dict]:
        """
        Simulate GET request
        In real code: use 'requests' library
        """
        try:
            url = self.build_url(endpoint)
            # TODO: In real usage, this would be:
            # response = requests.get(url, headers=self.headers)
            # return APIResponse(data=response.json())
            
            # For now, mock response:
            mock_data = {
                "users": [
                    {"id": 1, "name": "Alice"},
                    {"id": 2, "name": "Bob"}
                ]
            }
            return APIResponse(data=mock_data)
        
        except Exception as e:
            return APIResponse(error=str(e))
    
    def post(self, endpoint: str, body: dict) -> APIResponse[dict]:
        """Simulate POST request"""
        try:
            url = self.build_url(endpoint)
            # TODO: requests.post(url, json=body, headers=self.headers)
            return APIResponse(data={"success": True, "id": 123})
        
        except Exception as e:
            return APIResponse(error=str(e))


# ============================================================================
# USAGE EXAMPLE
# ============================================================================

if __name__ == "__main__":
    # Create client (like URLSession())
    client = APIClient("https://api.example.com")
    
    # Make request (like dataTask in Swift)
    response = client.get("users")
    
    # Handle response (like Swift's Result enum)
    if response.is_success():
        print("✅ Success!")
        print(json.dumps(response.data, indent=2))
    else:
        print(f"❌ Error: {response.error}")
    
    # POST request
    new_user = {"name": "Charlie", "email": "charlie@example.com"}
    response = client.post("users", new_user)
    
    if response.is_success():
        print(f"\n✅ User created: {response.data}")


# ============================================================================
# EXERCISE: Your Turn!
# ============================================================================

"""
TODO - Complete these exercises:

1. Add a DELETE method to APIClient
   - Signature: def delete(self, endpoint: str) -> APIResponse[bool]
   - Return success/failure

2. Add authentication
   - Add a 'token' parameter to __init__
   - Add Authorization header to requests

3. Create a User model class
   - class User:
   -     id: int
   -     name: str
   -     email: str

4. Parse the response into User objects
   - Modify get() to return APIResponse[list[User]]

Run this file to see it work:
$ python3 01_exercise_api_client.py
"""
