import paho.mqtt.client as mqtt
from sense_hat import SenseHat
import time
import csv
from datetime import datetime

# Initialize Sense HAT
sense = SenseHat()

# MQTT Broker details
BROKER = "localhost"  # Use "localhost" for local broker or IP address for remote broker
PORT = 1883
TOPIC = "sensehat/sensors"

# File to save the sensor data
CSV_FILE = "sensehat_data.csv"

# Function to write data to a CSV file
def write_to_csv(data):
    file_exists = False
    # Check if the file already exists
    try:
        with open(CSV_FILE, "r"):
            file_exists = True
    except FileNotFoundError:
        pass

    # Write data to CSV
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        # Write header if the file doesn't exist
        if not file_exists:
            writer.writerow(["Timestamp", "Temperature (C)", "Humidity (%)", "Pressure (hPa)"])
        writer.writerow(data)

# MQTT Client setup
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print(f"Failed to connect, return code {rc}")

def on_publish(client, userdata, mid):
    print(f"Message {mid} published.")

def on_disconnect(client, userdata, rc):
    print("Disconnected from MQTT Broker.")

# Setup MQTT Client
client = mqtt.Client("SenseHatPublisher")
client.on_connect = on_connect
client.on_publish = on_publish
client.on_disconnect = on_disconnect

# Connect to the broker
client.connect(BROKER, PORT, 60)

# Publishing data from Sense HAT
try:
    client.loop_start()
    while True:
        # Fetch data from Sense HAT
        temp = sense.get_temperature()
        humidity = sense.get_humidity()
        pressure = sense.get_pressure()
        calctemp = 0.0071*temp*temp+0.86*temp-10.0
        calchum=humidity*(2.5-0.029*temp)

        # Create a payload
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        payload = {
            "temperature": round(calctemp, 2),
            "humidity": round(calchum, 2),
            "pressure": round(pressure, 2),
        }
        print(f"Publishing: {payload}")

        # Save data to CSV
        csv_data = [timestamp, round(calctemp, 2), round(calchum, 2), round(pressure, 2)]
        write_to_csv(csv_data)

        # Publish to MQTT Topic
        client.publish(TOPIC, str(payload))
        time.sleep(5)  # Publish every 5 seconds

except KeyboardInterrupt:
    print("Exiting...")
finally:
    client.loop_stop()
    client.disconnect()
