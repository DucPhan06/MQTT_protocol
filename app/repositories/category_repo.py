#app.repositories.category
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.core.topics import normalize_topic
from app.models.category import Category
from app.core.categories import FIXED_CATEGORIES

ALLOWED_CATEGORY_MAP = {
    category["topic"]: category["name"]
    for category in FIXED_CATEGORIES
}

def save_category_if_new(db: Session, name: str) -> bool:

    topic = normalize_topic(name)

    if topic not in ALLOWED_CATEGORY_MAP:
        return False

    exist = db.scalars(select(Category).where(Category.topic == topic)).first()

    if exist:
        return False

    category = Category(
        name=ALLOWED_CATEGORY_MAP[topic],
        topic=topic,
    )

    db.add(category)
    db.commit()
    return True
