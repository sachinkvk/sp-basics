"""
EXERCISE 3: Data Models & JSON (Like Codable in Swift)

Swift's Codable → Python's Pydantic
"""

from dataclasses import dataclass, asdict
from typing import Optional, List
import json


# ============================================================================
# APPROACH 1: Dataclasses (Simple, Swift-like)
# ============================================================================

# Swift:
# struct User: Codable {
#     let id: Int
#     let name: String
#     let email: String?
# }

# Python with dataclasses:
@dataclass
class User:
    id: int
    name: str
    email: Optional[str] = None
    
    def to_dict(self) -> dict:
        """Convert to dictionary (like JSONEncoder)"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: dict) -> "User":
        """Create from dictionary (like JSONDecoder)"""
        return cls(**data)


# ============================================================================
# APPROACH 2: Pydantic (Recommended - better validation)
# ============================================================================

try:
    from pydantic import BaseModel, Field, field_validator
    
    class Post(BaseModel):
        id: int
        title: str
        content: str
        author_id: int
        views: int = 0  # Default value
        
        # Validation example
        @field_validator('title')
        @classmethod
        def title_not_empty(cls, v: str) -> str:
            if len(v.strip()) == 0:
                raise ValueError("Title cannot be empty")
            return v
        
        # Custom field name mapping (like @SerializedName in Android)
        # or CodingKeys in Swift
        class Config:
            populate_by_name = True
            json_schema_extra = {
                "example": {
                    "id": 1,
                    "title": "Example",
                    "content": "Content here",
                    "author_id": 1
                }
            }
    
    HAS_PYDANTIC = True

except ImportError:
    HAS_PYDANTIC = False
    Post = None


# ============================================================================
# PRACTICAL USAGE
# ============================================================================

def main():
    print("=== DATACLASSES (Simple) ===")
    
    # Create instance
    user = User(id=1, name="Alice", email="alice@example.com")
    print(f"User: {user}")
    
    # Convert to dict
    user_dict = user.to_dict()
    print(f"As dict: {user_dict}")
    
    # Convert to JSON
    user_json = json.dumps(user_dict)
    print(f"As JSON: {user_json}")
    
    # Parse from JSON
    parsed_json = '{"id": 2, "name": "Bob", "email": null}'
    parsed_dict = json.loads(parsed_json)
    user2 = User.from_dict(parsed_dict)
    print(f"Parsed user: {user2}")
    
    if HAS_PYDANTIC:
        print("\n=== PYDANTIC (With Validation) ===")
        
        # Create instance
        post = Post(
            id=1,
            title="My First Post",
            content="Hello, World!",
            author_id=1
        )
        print(f"Post: {post}")
        
        # Convert to JSON
        post_json = post.model_dump_json()
        print(f"As JSON: {post_json}")
        
        # Parse from JSON
        parsed = Post.model_validate_json(post_json)
        print(f"Parsed: {parsed}")
        
        # Validation example
        try:
            invalid = Post(
                id=2,
                title="",  # Empty title - will fail validation
                content="Test",
                author_id=1
            )
        except Exception as e:
            print(f"❌ Validation error: {e}")
    else:
        print("\n⚠️  Pydantic not installed. Install with: pip3 install pydantic")


# ============================================================================
# NESTED MODELS
# ============================================================================

@dataclass
class Comment:
    id: int
    text: str
    author: User


@dataclass
class PostWithComments:
    id: int
    title: str
    author: User
    comments: List[Comment]


def example_nested():
    print("\n=== NESTED MODELS ===")
    
    author = User(id=1, name="Alice")
    comment = Comment(id=1, text="Great post!", author=author)
    
    post = PostWithComments(
        id=1,
        title="My Post",
        author=author,
        comments=[comment]
    )
    
    print(f"Post with comments: {post}")
    
    # Convert to JSON
    post_dict = asdict(post)
    post_json = json.dumps(post_dict, indent=2)
    print(f"\nAs JSON:\n{post_json}")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    main()
    example_nested()
    
    print("\n" + "="*50)
    print("EXERCISES:")
    print("="*50)
    print("""
1. Create a Student model with:
   - id: int
   - name: str
   - email: str
   - gpa: float (with validation: 0.0 to 4.0)
   
2. Create a Course model with:
   - id: int
   - name: str
   - students: List[Student]
   - instructor: User

3. Serialize/deserialize a Course to/from JSON

4. (Advanced) Use Pydantic and add:
   - email validation (must have @)
   - gpa validation (0.0 to 4.0)
   - custom error messages
""")
