# app/services/mqtt_service.py

from app.schemas.news import NewsArticle
from app.mqtt.client import MQTTManager

TOPIC_ROOT = "news"

#TODO: Categorize topics by category, etc.
def article_topic(article: NewsArticle) -> str:
    topics = []

    for category in article.categories:
        topics.append(f"{TOPIC_ROOT}/{category}")

    return topics

def publish_article(mqtt_manager: MQTTManager, article: NewsArticle):
    if(article.duplicate):
        return
    
    topics = article_topic(article)
    payload = article.model_dump_json()
    for topic in topics:
        mqtt_manager.publish(topic, payload)