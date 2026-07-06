import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.mqtt.client import MQTTManager
from app.services.news_service import get_news
from app.services.article_service import normalize_articles
from app.services.mqtt_service import publish_article

REFETCH_TIME = 15

#TODO: avoid XSS in api

async def auto_fetch_news():
    while True:
        try:
            raw = get_news()
            data = normalize_articles(raw)
            print(data)

            for article in data:
                publish_article(app.state.mqtt, article)
        
        except Exception as e:
            print("News fetch task error:", e)
        
        await asyncio.sleep(REFETCH_TIME)

@asynccontextmanager
async def lifespan(app: FastAPI):
    #Start up create MQTT instances
    print("Application starting up...")
    client1 = MQTTManager("", "12345678")
    client1.connect()
    app.state.mqtt = client1

    task = asyncio.create_task(auto_fetch_news())

    yield

    #Shutdown: disconnect all MQTT instances
    print("Application shutting down...")
    task.cancel()
    app.state.mqtt.disconnect() 



app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}
