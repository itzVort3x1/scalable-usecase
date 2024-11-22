
host=$(hostname | cut -d'-' -f2)

echo "The host is: $host"

case $host in
  003)
    python3 satellite.py &
    echo "Satellites switched one\..."
    ;;
  004)
    python3 clinic.py &
    echo "Clinic up and running..."
    ;;
  007)
    python3 satellite.py &
    echo "Satellites switched one\..."
    ;;
  017)
    python3 centralCommunication.py &
    echo "Centra communication ready to receive connections..."
    ;;
  025)
    python3 satellite.py &
    echo "Satellites switched one\..."
    ;;
  027)
    python3 satellite.py &
    echo "Satellites switched one\..."
    ;;
  028)
    python3 satellite.py &
    echo "Satellites switched one\..."
    ;;
esac