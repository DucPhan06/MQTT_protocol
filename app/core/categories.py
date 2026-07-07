FIXED_CATEGORIES = [
    {"name": "Business", "topic": "business"},
    {"name": "Entertainment", "topic": "entertainment"},
    {"name": "Environment", "topic": "environment"},
    {"name": "Food", "topic": "food"},
    {"name": "Health", "topic": "health"},
    {"name": "Politics", "topic": "politics"},
    {"name": "Science", "topic": "science"},
    {"name": "Sports", "topic": "sports"},
    {"name": "Technology", "topic": "technology"},
    {"name": "Top", "topic": "top"},
    {"name": "World", "topic": "world"},
    {"name": "General", "topic": "general"},
]

ALLOWED_CATEGORY_TOPICS = {category["topic"] for category in FIXED_CATEGORIES}
