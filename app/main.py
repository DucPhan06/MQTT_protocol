import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.sessions import SessionLocal
from app.mqtt.client import MQTTManager
from app.repositories.article_repo import save_article_if_new
from app.services.news_service import get_news
from app.services.article_service import normalize_articles
from app.services.mqtt_service import publish_article
from app.core.mqtt_config import NEWS_FETCH_TIMER

#TODO: avoid XSS in api

async def auto_fetch_news(mqtt: MQTTManager):    
    while True:

        db = SessionLocal()

        try:
            raw = get_news()
            data = normalize_articles(raw)
            print(data)

            for article in data:
                is_new = save_article_if_new(db, article)

                if is_new:
                    publish_article(mqtt, article)
                else:
                    print("Duplicate article, skipping publish.\n")
        
        except Exception as e:
            db.rollback()
            print("News fetch task error:", e)

        finally:
            db.close()
        
        await asyncio.sleep(NEWS_FETCH_TIMER)

@asynccontextmanager
async def lifespan(app: FastAPI):
    #Start up create MQTT instances
    print("Application starting up...")
    client1 = MQTTManager("", "12345678")
    client1.connect()
    app.state.mqtt = client1

    task = asyncio.create_task(auto_fetch_news(client1))

    yield

    #Shutdown: disconnect all MQTT instances
    print("Application shutting down...")
    task.cancel()
    app.state.mqtt.disconnect() 



app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}
