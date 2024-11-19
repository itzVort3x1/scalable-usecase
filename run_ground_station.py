from components.groundstation.ground_station import GroundStation

if __name__ == "__main__":
    # Start the ground station
    ground_station = GroundStation(
        receive_port=33000,
        send_port=34000,
        adjacency_list_file="./protocol/discovery/adjacency_list.json",
        storage_path="./data"
    )
    ground_station.start_receiver()
