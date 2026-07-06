#app.services.article_service.py

from app.schemas.news import NewsArticle

ALLOWED_CATEGORIES = {
    "business",
    "entertainment",
    "environment",
    "food",
    "health",
    "politics",
    "science",
    "sports",
    "technology",
    "top",
    "world",
    "general",
}

TOPIC_ROOT = "news"

def normalize_article(raw: dict) -> NewsArticle:
    return NewsArticle(
        article_id = raw.get("article_id") or "",
        title = raw.get("title") or "",
        link = raw.get("link") or "",
        source = raw.get("source_name") or raw.get("source") or "",
        category = resolve_category(raw.get("category")),
        published_at = raw.get("pubDate") or "",
        duplicate =  bool(raw.get("duplicate", False))
    )

def normalize_articles(raw_articles: list[dict]) -> list[NewsArticle]:
    for i in range(len(raw_articles)):
        raw_articles[i] = normalize_article(raw_articles[i])
    return raw_articles

def resolve_category(category) -> str:
    if isinstance(category, list):  
        category = category[0] if category[0] in ALLOWED_CATEGORIES else "general"
    elif not isinstance(category, str):
        category = "general"
    
    return category
 