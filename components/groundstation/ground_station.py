import json
from protocol.jarvis import Jarvis


class GroundStation:
    def __init__(self, receive_port=33000, send_port=34000, adjacency_list_file="./discovery/adjacency_list.json", storage_path="./data"):
        self.jarvis = Jarvis(
            receive_port=receive_port,
            send_port=send_port,
            adjacency_list_file=adjacency_list_file,
        )
        self.local_ip = self.jarvis.local_ip
        self.neighbors = self.get_neighbors()
        self.storage_path = storage_path

    def get_neighbors(self):
        """Retrieve neighbors from the adjacency list."""
        return self.jarvis.adjacency_list.get(self.local_ip, {})

    def handle_message(self, data):
        """Process incoming messages."""
        message = self.jarvis.parse_message(data)
        print(f"Ground Station {self.local_ip} received message: {message['message_content']}")
        self.store_data(message["message_content"])

    def store_data(self, data):
        """Store the received data locally."""
        with open(f"{self.storage_path}/data.json", "a") as file:
            file.write(json.dumps(data) + "\n")
        print(f"Data stored at ground station {self.local_ip}: {data}")

    def start_receiver(self):
        """Start the ground station's receiver."""
        self.jarvis.start_receiver(self.store_data)
