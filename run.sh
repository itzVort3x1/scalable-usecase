#!/bin/bash

# Function to run all components
run_all() {
    echo "Starting Scalable Usecase System (Group 4)..."

    python3 run_ground_station.py &
    echo "Centra communication ready to receive connections..."

    python3 run_satellite.py &
    echo "Satellites switched one\..."

    python3 run_sensor.py &
    echo "Clinic up and running..."
}

run_all
