import asyncio
import uuid
import sys
import math

from app.mqtt.client import MQTTManager
from app.services.simulation_service import SimulationService

def print_response(client_id: str, topic: str):
    print(f"client {client_id} subscribes to {topic} received a news.\n")

#divide topics choice to 4 choice: business, top, politics, food 
def topics_choice(index: int, total: int) -> str:
    section = math.floor(total/4)

    if(index < section): return "news/v1/business"
    if(index < section*2): return "news/v1/top"
    if(index < section*3): return "news/v1/politics"
    return "news/v1/food"

async def main():
    client_num = 1
    clients = []
    simul = SimulationService()

    if (len(sys.argv) > 1 and int(sys.argv[1]) > 0):
        client_num = int(sys.argv[1])

    for i in range(client_num):
        client_id = str(f"client_{i}_{uuid.uuid4()}")
        topic = topics_choice(i, client_num)
        
        client = MQTTManager(client_id, topic, on_client_connect=simul.record_client, on_message_received=print_response)

        client.connect()

        clients.append(client)

        #avoid too many tls connect at once to the broker
        await asyncio.sleep(0.05)
        
    try:
        while True:
            print(f"Number of clients connected: {simul.get_total_clients()}/{client_num}")
            await asyncio.sleep(5)  

    finally:
        for client in clients:
            client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
