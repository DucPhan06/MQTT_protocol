# app/services/mqtt_service.py

from app.schemas.news import NewsArticle
from app.mqtt.client import MQTTManager

TOPIC = [
    "test"
]

#TODO: Categorize topics by category, etc.
def news_topic(article: NewsArticle) -> str:
    return "test"

def publish_article(mqtt_manager: MQTTManager, article: NewsArticle):
    topic = news_topic(article)
    payload = article.model_dump_json()
    mqtt_manager.publish(topic, payload)