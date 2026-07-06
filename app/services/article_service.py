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

def normalize_article(raw: dict) -> NewsArticle:
    return NewsArticle(
        article_id = parse_string(raw.get("article_id")),
        title = parse_string(raw.get("title")),
        link = parse_string(raw.get("link")),
        source_name = parse_string(raw.get("source_name")),
        source_id = parse_string(raw.get("source_id")),
        categories = resolve_category(list(raw.get("category"))),
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

def resolve_category(raw_category: list) -> list:
    categories = set()

    for cat in raw_category:
        if cat in ALLOWED_CATEGORIES:
            categories.add(cat)
        else:
            categories.add("general")
    
    return list(categories)
 
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