# app/services/mqtt_service.py

from app.schemas.news import NewsArticle
from app.mqtt.client import MQTTManager
from app.services.topic_service import build_article_topics

def publish_article(mqtt_manager: MQTTManager, article: NewsArticle):
    if(article.duplicate):
        return
    
    topics = build_article_topics(article)
    print(topics)
    payload = article.model_dump_json()
    for topic in topics:
        mqtt_manager.publish(topic, payload, 1) #Choose QoS 1 to avoid dropping message but Postgre still record
                                                #TODO: fix the saving logic