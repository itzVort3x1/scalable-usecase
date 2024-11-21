
# **Scalable Usecase System (Group 2)**

## **Overview**
- **Clinics**: They send data to the central communication or to hospitals in the urban area.
- **Satellites**: They help in communicating from rural areas to urban areas by re transmitting the message.
- **central communication**: This module can receive data from clinics in rural areas. 

### 1. **Required Dependencies**
This project requires Python 3. Install the dependencies:
```bash
pip install cryptography
```

### 2. **Generate RSA Keys**
Run the `generate_keys.py` script to generate RSA key files:
```bash
python3 generate_keys.py
```
The keys will be saved in the `protocol/crypto/` directory:
- `private_key.pem`
- `public_key.pem`


---
## **Running the System**

### 1. **Run All Components**
Use the `run.sh` script to start all components:
```bash
./run.sh
```

### 2. **Run Components Individually**
You can run each component separately for debugging or testing:
- **Sensor**:
    ```bash
    python3 run_sensor.py
    ```
- **Satellite**:
    ```bash
    python3 run_satellite.py
    ```
- **Ground Station**:
    ```bash
    python3 run_ground_station.py
    ```

---

## **Features**
1. **Secure Communication**:
   - Messages are encrypted using RSA.
   - Integrity is verified using CRC32 checksums.

2. **Routing and Relaying**:
   - Sensors send data to linked satellites.
   - Satellites broadcast to other satellites and relay to the ground station.

3. **Fire Detection**:
   - Alerts are triggered if thresholds for temperature or smoke levels are exceeded.

4. **Data Storage**:
   - The ground station stores all received data locally in JSON format.

---

## **Future Enhancements**
1. **Dynamic Routing**: Implement adaptive routing based on network conditions.
2. **Fault Tolerance**: Add retry mechanisms for failed transmissions.
3. **Dashboard**: Develop a web-based interface to visualize data and alerts.

---

