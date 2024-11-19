#!/bin/bash

# Function to run all components
run_all() {
    echo "Starting Scalable Usecase System (Group 4)..."

    # Start the Ground Station
    python3 run_ground_station.py &
    echo "Ground Station started..."

    # Start the Satellites
    python3 run_satellite.py &
    echo "Satellites started..."

    # Start the Sensors
    python3 run_sensor.py &
    echo "Sensors started..."

    echo "System is now running."
}

# Entry point
run_all
