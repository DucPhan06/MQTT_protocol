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
        categories = resolve_category(list(raw.get("category"))),
        published_at = raw.get("pubDate") or "",
        duplicate =  bool(raw.get("duplicate", False))
    )

def normalize_articles(raw_articles: list[dict]) -> list[NewsArticle]:
    for i in range(len(raw_articles)):
        raw_articles[i] = normalize_article(raw_articles[i])
    return raw_articles

def resolve_category(raw_category: list) -> list:
    categories = set()

    for cat in raw_category:
        if cat in ALLOWED_CATEGORIES:
            categories.add(cat)
        else:
            categories.add("general")
    
    return list(categories)
 