import asyncio
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.mqtt.client import MQTTManager
from app.services.news_service import get_news

REFETCH_TIME = 15

async def auto_fetch_news():
    while True:
        data = get_news()
        article_test = []
        for article in data:
            article_test.append(article)
            if len(article_test) == 3:
                break
        
        for article in article_test:
            app.state.mqtt.publish("test", article["title"])
        
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
