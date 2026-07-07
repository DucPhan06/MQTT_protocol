#app.services.article_service.py

from sqlalchemy.orm import Session

from app.repositories import article_repo
from app.repositories.category_repo import save_category_if_new
from app.schemas.news import NewsArticle
from app.services import mqtt_service, topic_service

def process_article(db, mqtt_manager, article: NewsArticle):
    if article.duplicate:
        return False

    saved = article_repo.save_article_if_new(db, article)

    print(f"saved: {saved}")

    if not saved:
        return False

    topics = topic_service.build_article_topics(article)
    payload = article.model_dump_json()

    print(f"topics: {topics}")
    print(f"payload: {payload}")

    mqtt_service.publish_to_topics(mqtt_manager, article, topics, payload)

    return True

def save_article_categories(db: Session, article: NewsArticle) -> None:
    for category in article.categories:
        save_category_if_new(db, category)

def normalize_article(raw: dict) -> NewsArticle:
    return NewsArticle(
        article_id = parse_string(raw.get("article_id")),
        title = parse_string(raw.get("title")),
        link = parse_string(raw.get("link")),
        source_name = parse_string(raw.get("source_name")),
        source_id = parse_string(raw.get("source_id")),
        categories = parse_string_list(raw.get("category")),
        language = parse_string_list(raw.get("language")),
        country = parse_string_list(raw.get("country")),
        fetched_at = parse_string(raw.get("fetched_at")),
        published_at = parse_string(raw.get("pubDate")),
        duplicate =  parse_bool(raw.get("duplicate"))
    )

def normalize_articles(raw_articles: list[dict]) -> list[NewsArticle]:
    for i in range(len(raw_articles)):
        raw_articles[i] = normalize_article(raw_articles[i])
    return raw_articles
 
def parse_string_list(raw) -> list[str]:
    if isinstance(raw, list):
        for i in range(len(raw)):
            raw[i] = str(raw[i])
        return raw

    if isinstance(raw, str):
        return [raw]

    return []

def parse_string(raw) -> str:
    if isinstance(raw, str):
        return raw
    return ""

def parse_bool(raw) -> bool:
    if isinstance(raw, bool):
        return raw

    if isinstance(raw, str):
        return raw.lower() == "true"

    return False