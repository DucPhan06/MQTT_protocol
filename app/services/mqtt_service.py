# app/services/mqtt_service.py

from app.schemas.news import NewsArticle
from app.mqtt.client import MQTTManager
from app.services.topic_service import build_article_topics

TOPIC_ROOT = "news"

def publish_article(mqtt_manager: MQTTManager, article: NewsArticle):
    if(article.duplicate):
        return
    
    topics = build_article_topics(article)
    payload = article.model_dump_json()
    for topic in topics:
        mqtt_manager.publish(topic, payload)