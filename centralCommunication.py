from services.central import Central

if __name__ == "__main__":
    ground_station = Central(
        receive_port=33000,
        send_port=34000,
        adjacency_list_file="./protocol/discovery/adjacency_list.json",
        storage_path="./data"
    )
    ground_station.accept_connections()
