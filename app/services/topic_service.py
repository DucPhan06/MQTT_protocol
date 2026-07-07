from app.repositories.category_repo import normalize_topic
from app.schemas.news import NewsArticle
from app.core.categories import ALLOWED_CATEGORY_TOPICS

TOPIC_ROOT = "news"
TOPIC_VER = "v1"

def build_topic(category_topic: str) -> str:
    return f"{TOPIC_ROOT}/{TOPIC_VER}/{category_topic}"

def build_article_topics(article: NewsArticle) -> list[str]:
    topics = []

    categories = article.categories or ["general"]

    for category in categories:
        category_topic = normalize_topic(category)

        if category_topic not in ALLOWED_CATEGORY_TOPICS:
            category_topic = "general"

        mqtt_topic = build_topic(category_topic)

        print("mqtt topics: ", mqtt_topic)

        topics.append(mqtt_topic)

    return topics
    