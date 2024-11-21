import json
from protocol.jarvis import Jarvis


class Central:
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
        return self.jarvis.adjacency_list.get(self.local_ip, {})

    def handle_message(self, data):
        message = self.jarvis.parse_message(data)
        self.store_data(message["message_content"])

    def store_data(self, data):
        with open(f"{self.storage_path}/data.json", "a") as file:
            file.write(json.dumps(data) + "\n")
        print(f"Data stored at ground station {self.local_ip}: {data}")

    def accept_connections(self):
        self.jarvis.start_receiver(self.store_data)
