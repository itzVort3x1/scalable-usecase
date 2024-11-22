import threading
from services.clinic import Clinic
import signal
import sys

# Global list to hold Clinic instances
clinic_instances = []

def start_sensor_instance(receive_port, send_port):
    clinic = Clinic(
        receive_port=receive_port,
        send_port=send_port,
        adjacency_list_file="./protocol/discovery/adjacency_list.json"
    )
    clinic_instances.append(clinic)
    clinic.start()

def signal_handler(signal, frame):
    print("Gracefully stopping all clinics...")
    for clinic in clinic_instances:
        clinic.stop()
    sys.exit(0)

if __name__ == "__main__":
    # Register the signal handler for clean shutdown
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    clinic_config = [{"receive_port": 33000, "send_port": 34000}]

    threads = []
    for config in clinic_config:
        thread = threading.Thread(
            target=start_sensor_instance,
            args=(config["receive_port"], config["send_port"])
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
