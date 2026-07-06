from app.schemas.news import NewsArticle

TOPIC_ROOT = "news"
TOPIC_VER = "v1"

def build_article_topics(article: NewsArticle) -> list[str]:
    topics = []

    for category in article.categories:
        topics.append(f"{TOPIC_ROOT}/{TOPIC_VER}/{category}")

    return topics
    