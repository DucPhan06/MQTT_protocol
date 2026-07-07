# app/services/mqtt_service.py

from app.schemas.news import NewsArticle
from app.mqtt.client import MQTTManager

def publish_to_topics(mqtt_manager: MQTTManager, article: NewsArticle, topics, payload, qos=1):    
    for topic in topics:
        mqtt_manager.publish(topic, payload, qos) #Choose QoS 1 to avoid dropping message but Postgre still record
                                                #TODO: fix the saving logic