#app.services.simulation_service.py


class SimulationService:
    def __init__(self):
        self.connected_clients = 0
    
    def record_client(self, client_id: str):
        self.connected_clients += 1

    def get_total_clients(self) -> int:
        return self.connected_clients