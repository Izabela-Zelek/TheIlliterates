import paho.mqtt.client as mqtt
from sense_hat import SenseHat
import time
import csv
import random

sense = SenseHat()

mqtt_client = mqtt.Client()
broker_address = "localhost" #Replace with Chris' address
mqtt_client.connect(broker_address)

def save_data():
    temperature = random.randrange(10,30)
    humidity = random.randrange(0, 15)
    with open("data.csv", "a", newline='') as data_file:
        writer = csv.writer(data_file)
        writer.writerow([time.strftime('%Y-%m-%d %H:%M:%S'), temperature, humidity])
        print("Data uploaded")
        
def publish_context(context_message):
    mqtt_client.publish("testing/subscribe", context_message)
    print(f"Published context: {context_message}")
    
def main():
    try:
        while True:
            save_data()
            time.sleep(5)
            publish_context("Yeehaw")
    except KeyboardInterrupt:
        sense.clear()
        print("Bye bye")
        
if __name__ == "__main__":
    main()
        