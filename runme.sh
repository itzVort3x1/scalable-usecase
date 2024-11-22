#!/bin/bash

# Get the host part of the hostname
host=$(hostname | cut -d'-' -f2)
pid_file="/tmp/related_processes.pid"

# Function to handle cleanup on SIGINT (Ctrl+C) or SIGTERM
cleanup() {
  echo -e "\nKeyboardInterrupt detected. Stopping all processes..."
  if [[ -f $pid_file ]]; then
    while read -r pid; do
      kill "$pid" 2>/dev/null && echo "Stopped process $pid"
    done < "$pid_file"
    rm -f "$pid_file"
  fi
  echo "All processes stopped. Exiting."
  exit 0
}

# Set trap for SIGINT and SIGTERM
trap cleanup SIGINT SIGTERM

# Clear the PID file (if it exists)
> "$pid_file"

# Start processes based on the host
echo "The host is: $host"

case $host in
  003)
    python3 satellite.py & echo $! >> "$pid_file"
    echo "Satellites switched on..."
    ;;
  004)
    python3 clinic.py & echo $! >> "$pid_file"
    echo "Clinic up and running..."
    ;;
  007)
    python3 satellite.py & echo $! >> "$pid_file"
    echo "Satellites switched on..."
    ;;
  017)
    python3 centralCommunication.py & echo $! >> "$pid_file"
    echo "Central communication ready to receive connections..."
    ;;
  025)
    python3 satellite.py & echo $! >> "$pid_file"
    echo "Satellites switched on..."
    ;;
  027)
    python3 satellite.py & echo $! >> "$pid_file"
    echo "Satellites switched on..."
    ;;
  028)
    python3 satellite.py & echo $! >> "$pid_file"
    echo "Satellites switched on..."
    ;;
esac

# Keep the script running to wait for interrupt (simulate a long-running service)
echo "Press Ctrl+C to stop the processes."
while true; do
  sleep 1
done
