import asyncio
import uuid
import sys

from app.mqtt.client import MQTTManager
from app.services.simulation_service import SimulationService

def increment_client(num: int):
    num += 1

async def main():
    connected_client = 0
    client_num = 1
    clients = []
    simul = SimulationService()

    if (len(sys.argv) > 1 and int(sys.argv[1]) > 0):
        client_num = int(sys.argv[1])

    for i in range(client_num):
        client_id = str(f"client_{i}_{uuid.uuid4()}")
        client = MQTTManager(client_id, "news/v1/#", on_client_connect=simul.record_client)

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
