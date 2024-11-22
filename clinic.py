import threading
from services.clinic import Clinic


def start_sensor_instance(receive_port, send_port):
    clinic = Clinic(
        receive_port=receive_port,
        send_port=send_port,
        adjacency_list_file="./protocol/discovery/adjacency_list.json"
    )
    try:
        clinic.start()
    except KeyboardInterrupt:
        clinic.stop()


if __name__ == "__main__":
    clinic_config = [{"receive_port": 33000, "send_port": 34000}]

    threads = []
    for config in clinic_config:
        thread = threading.Thread(
            target=start_sensor_instance,
            args=(config["receive_port"], config["send_port"]),
            daemon=True
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
