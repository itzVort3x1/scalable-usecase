from protocol.jarvis import Jarvis


class Satellite:
    def __init__(self, receive_port=33000, send_port=34000, adjacency_list_file="./discovery/adjacency_list.json"):
        self.jarvis = Jarvis(
            receive_port=receive_port,
            send_port=send_port,
            adjacency_list_file=adjacency_list_file,
        )
        self.local_ip = self.jarvis.local_ip
        self.neighbors = self.get_neighbors()

    def get_neighbors(self):
        return self.jarvis.adjacency_list.get(self.local_ip, {})

    def handle_message(self, data):
        message = self.jarvis.parse_message(data)

        if message["dest_ip"] == self.jarvis.local_ip:
            print(f"Message delivered to satellite {self.local_ip}.")
        else:
            self.forward_message(message)

    def forward_message(self, message):
        _, previous_nodes = self.jarvis.dijkstra(self.jarvis.adjacency_list, self.local_ip)
        next_hop = self.jarvis.get_next_hop(previous_nodes, self.local_ip, message["dest_ip"])
        if next_hop:
            print(f"Satellite {self.local_ip} forwarding message to next hop: {next_hop}")
            self.jarvis.forward_message(message, next_hop)
        else:
            print(f"Satellite {self.local_ip} could not find a route to {message['dest_ip']}. Dropping packet.")

    def start_receiver(self):
        self.jarvis.start_receiver()
