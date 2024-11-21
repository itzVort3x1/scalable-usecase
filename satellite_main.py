from services.satellite import Satellite

if __name__ == "__main__":
    # Start the satellite
    satellite = Satellite(
        receive_port=33000,
        send_port=34000,
        adjacency_list_file="./protocol/discovery/adjacency_list.json"
    )
    satellite.start_receiver()
