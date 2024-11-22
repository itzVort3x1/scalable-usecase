
# **Scalable Usecase System (Group 2)**

# Protocol buit in collaboration with group 4

## **Overview**
- **Clinics**: They send data to the central communication or to hospitals in the urban area.
- **Satellites**: They help in communicating from rural areas to urban areas by re transmitting the message.
- **central communication**: This module can receive data from clinics in rural areas. 

### 1. **Required Dependencies**
This project requires Python 3. Install the dependencies:

`pip install cryptography==2.8`


### 2. **Generate RSA Keys**
## Note this is only required first time, but I have provided the keys in the folder structure so this command is not required to run.
Run the `generate_keys.py` script to generate RSA key files:
```bash
python3 generate_keys.py
```
The keys will be saved in the `protocol/crypto/` directory:
- `private_key.pem`
- `public_key.pem`


---
## **Running the System**

### 1. **Run All Components**Use the `runme.sh` script to start the components:
```bash
./runme.sh
```

NOTE: This command will have to be run in all the Pi's of group-2 and 4, and the Pi numbers are: 3,4,25,28,27,17,7. In order for it to function properly. 

### 2. **Run Components Individually**
You can run each component separately for debugging or testing:
- **clinic**:
    ```bash
    python3 clinic.py
    ```
- **Satellite**:
    ```bash
    python3 satellite.py
    ```
- **Central Communication**:
    ```bash
    python3 centralCommunication.py
    ```

