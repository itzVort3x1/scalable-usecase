import threading
from components.sensors.sensor import Sensor


def start_sensor_instance(sensor_id, receive_port, send_port):
    """Start a single sensor instance."""
    print(f"Starting Sensor {sensor_id} on ports {receive_port} (receive) and {send_port} (send)...")
    sensor = Sensor(
        receive_port=receive_port,
        send_port=send_port,
        adjacency_list_file="./protocol/discovery/adjacency_list.json"
    )
    sensor.start()


if __name__ == "__main__":
    # Configuration for five sensors with unique ports
    # sensors_config = [
    #     {"sensor_id": "S1", "receive_port": 33001, "send_port": 33006},
    #     {"sensor_id": "S2", "receive_port": 33002, "send_port": 33007},
    #     {"sensor_id": "S3", "receive_port": 33003, "send_port": 33008},
    #     {"sensor_id": "S4", "receive_port": 33004, "send_port": 33009},
    #     {"sensor_id": "S5", "receive_port": 33005, "send_port": 33010},
    # ]
    sensors_config = [{"sensor_id": "S1", "receive_port": 33000, "send_port": 34000}]

    # Start each sensor in its own thread
    threads = []
    for config in sensors_config:
        thread = threading.Thread(
            target=start_sensor_instance,
            args=(config["sensor_id"], config["receive_port"], config["send_port"]),
            daemon=True
        )
        threads.append(thread)
        thread.start()

    # Keep the main thread alive to allow sensors to run
    for thread in threads:
        thread.join()
