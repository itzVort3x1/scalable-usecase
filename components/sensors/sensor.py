import time
import json
from protocol.jarvis import Jarvis
import random
from data_generator import mock_smartwatch_data


class Sensor:
    def __init__(self, receive_port=33000, send_port=34000, adjacency_list_file="./discovery/adjacency_list.json"):
        self.jarvis = Jarvis(
            receive_port=receive_port,
            send_port=send_port,
            adjacency_list_file=adjacency_list_file,
        )
        self.local_ip = self.jarvis.local_ip
        self.neighbors = self.get_neighbors()

    def get_neighbors(self):
        """Retrieve neighbors from the adjacency list."""
        return self.jarvis.adjacency_list.get(self.local_ip, {})

    def generate_data(self):
        return mock_smartwatch_data()

    def send_data(self):
        """Send data to the hardcoded destination IP."""
        dest_ip = "10.35.70.17"  # Hardcoded destination IP

        data = self.generate_data()
        print(f"Sensor {self.local_ip} generated data: {data}")
        print(f"Sensor {self.local_ip} sending data to hardcoded destination: {dest_ip}")

        self.jarvis.send_message(dest_ip=dest_ip, message=data)

    def handle_message(self, data):
        """Handle incoming messages, such as ACKs."""
        message = self.jarvis.parse_message(data)
        print(f"Sensor {self.local_ip} received message: {message['message_content']}")

        # Handle ACK message
        if message["message_type"] == "ACK":
            print(f"Sensor {self.local_ip} received ACK for message ID: {message['message_id']}")

    def start_receiver(self):
        """Start the sensor's receiver to handle incoming messages."""
        self.jarvis.start_receiver()

    def start(self):
        """Start both sending data and receiving messages."""
        # Start the receiver in a separate thread
        import threading
        threading.Thread(target=self.start_receiver, daemon=True).start()

        # Periodically send data
        while True:
            self.send_data()
            time.sleep(5)
