from fastapi import FastAPI
from pydantic import BaseModel
from contextlib import asynccontextmanager
from app.mqtt.client import MQTTManager
from app.services.news_service import get_news


@asynccontextmanager
async def lifespan(app: FastAPI):
    #Start up create MQTT instances
    print("Application starting up...")
    client1 = MQTTManager("", "12345678")
    client1.connect()
    app.state.mqtt = client1
    
    data = get_news()
    article_test = []
    for article in data:
        article_test.append(article)
        if len(article_test) == 3:
            break
    
    for article in article_test:
        client1.publish("test", article["title"])


    yield

    #Shutdown: disconnect all MQTT instances
    print("Application shutting down...")
    app.state.mqtt.disconnect()



app = FastAPI(lifespan=lifespan)


# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: bool | None = None

@app.get("/")
def read_root():
    return {"Hello": "World"}




# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}