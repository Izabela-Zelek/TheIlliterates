import paho.mqtt.client as mqtt
from sense_hat import SenseHat
import time
import random
from datetime import datetime
import json

#Due to a lack of light sensor, data is randomly generated based on month and hour
def calculate_sample_light(month, hour):
    light = 0;
    if 2 <= month <= 4:
        if 8 <= hour <= 15:
            light = random.randint(0,300)
        elif 16 <= hour <= 18:
            light = random.randint(0-600)
        elif 19 <= hour <= 22:
            light = random.randint(300-600)
        else:
            light = random.randint(0,300)
    elif 5 <= month <= 7:
        if 22 <= hour <= 23:
            light = random.randint(0,600)
        else:
            light = 0
    elif 8 <= month <= 10:
        if 16 <= hour <= 20:
            light = random.randint(0,300)
        elif 21 <= hour <= 22:
            light = random.randint(300,600)
        else:
            light = 0
    else:
        if 18 <= hour <= 22:
            light = random.randint(300,600)
        else:
            light = random.randint(0,300)
    return light

#Defines a fire animation which runs when fire detected
def fire_animation():
    for i in range(1, 11): 
        pixels = [
             B, R, R, B, B, B, O, B,
             B, B, O, R, R, B, B, B,
             B, B, R, O, R, R, B, B,
             B, R, R, O, O, R, R, B,
             R, R, O, O, O, O, O, R,
             R, O, O, Y, Y, Y, O, R,
             R, R, Y, Y, B, Y, R, B,
             B, R, R, B, B, R, B, B,
        ]
        sense.set_pixels(pixels)
        time.sleep(0.5)
        pixels = [
             B, B, B, R, R, B, B, B,
             B, B, B, R, O, R, B, O,
             B, B, R, O, O, R, R, B,
             B, R, R, O, O, O, R, B,
             R, R, O, O, Y, O, O, R,
             R, O, O, Y, Y, Y, O, R,
             R, R, Y, Y, B, Y, R, B,
             B, R, R, B, B, R, B, B,
        ]
        sense.set_pixels(pixels)
        time.sleep(0.5)

        sense.clear()

#Defines a gas animation which runs when fire detected
def gas_animation():
    for i in range(1, 11):
        pixels = [
             L, L, W, L, B, B, B, B,
             G, L, L, L, B, B, G, B,
             G, G, G, B, B, B, G, B,
             B, B, B, B, B, L, L, G,
             B, B, B, B, B, L, L, W,
             B, B, B, B, G, L, L, W,
             B, B, B, B, G, G, L, L,
             B, B, B, B, B, G, G, G,
        ]
        sense.set_pixels(pixels)
        time.sleep(0.1)
        pixels = [
             G, L, L, L, B, B, G, B,
             G, G, G, B, B, B, G, B,
             B, B, B, B, B, L, L, G,
             B, B, B, B, B, L, L, W,
             B, B, B, B, G, L, L, W,
             B, G, B, B, G, G, L, L,
             B, G, B, B, B, G, G, G,
             L, L, G, B, B, B, B, B,
        ]
        sense.set_pixels(pixels)
        time.sleep(0.1)
        pixels = [
             G, G, G, B, B, B, G, B,
             B, B, B, B, B, L, L, G,
             B, B, B, B, B, L, L, W,
             B, B, B, B, G, L, L, W,
             B, G, B, B, G, G, L, L,
             B, G, B, B, B, G, G, G,
             L, L, G, B, B, B, B, B,
             L, L, W, B, B, B, B, B,
        ]
        sense.set_pixels(pixels)
        time.sleep(0.1)
        pixels = [
             B, B, B, B, B, L, L, G,
             B, B, B, B, B, L, L, W,
             B, B, B, B, G, L, L, W,
             B, G, B, B, G, G, L, L,
             B, G, B, B, B, G, G, G,
             L, L, G, B, B, B, B, B,
             L, L, W, B, B, B, B, B,
             L, L, W, L, B, B, B, B,
        ]
        sense.set_pixels(pixels)
        time.sleep(0.1)
        pixels = [
             B, B, B, B, B, L, L, W,
             B, B, B, B, G, L, L, W,
             B, G, B, B, G, G, L, L,
             B, G, B, B, B, G, G, G,
             L, L, G, B, B, B, B, B,
             L, L, W, B, B, B, B, B,
             L, L, W, L, B, B, B, B,
             G, L, L, L, B, B, G, B,
        ]
        sense.set_pixels(pixels)
        time.sleep(0.1)
        pixels = [
             B, B, B, B, G, L, L, W,
             B, G, B, B, G, G, L, L,
             B, G, B, B, B, G, G, G,
             L, L, G, B, B, B, B, B,
             L, L, W, B, B, B, B, B,
             L, L, W, L, B, B, B, B,
             G, L, L, L, B, B, G, B,
             G, G, G, B, B, B, G, B,
        ]
        sense.set_pixels(pixels)
        time.sleep(0.1)
        pixels = [
             B, G, B, B, G, G, L, L,
             B, G, B, B, B, G, G, G,
             L, L, G, B, B, B, B, B,
             L, L, W, B, B, B, B, B,
             L, L, W, L, B, B, B, B,
             G, L, L, L, B, B, G, B,
             G, G, G, B, B, B, G, B,
             B, B, B, B, B, L, L, G,
        ]
        sense.set_pixels(pixels)
        time.sleep(0.1)
        pixels = [
             B, G, B, B, B, G, G, G,
             L, L, G, B, B, B, B, B,
             L, L, W, B, B, B, B, B,
             L, L, W, L, B, B, B, B,
             G, L, L, L, B, B, G, B,
             G, G, G, B, B, B, G, B,
             B, B, B, B, B, L, L, G,
             B, B, B, B, B, L, L, W,
        ]
        sense.set_pixels(pixels)
        time.sleep(0.1)
        pixels = [
             L, L, G, B, B, B, B, B,
             L, L, W, B, B, B, B, B,
             L, L, W, L, B, B, B, B,
             G, L, L, L, B, B, G, B,
             G, G, G, B, B, B, G, B,
             B, B, B, B, B, L, L, G,
             B, B, B, B, B, L, L, W,
             B, B, B, B, G, L, L, W,
        ]
        sense.set_pixels(pixels)
        time.sleep(0.1)
        pixels = [
             L, L, W, B, B, B, B, B,
             L, L, W, L, B, B, B, B,
             G, L, L, L, B, B, G, B,
             G, G, G, B, B, B, G, B,
             B, B, B, B, B, L, L, G,
             B, B, B, B, B, L, L, W,
             B, B, B, B, G, L, L, W,
             B, B, B, B, G, G, L, L,
        ]
        sense.set_pixels(pixels)
        time.sleep(0.1)
        sense.clear()
            
def publish_context(context_message):
    mqtt_client.publish("sending/sensorData", context_message)
    print(f"Published context: {context_message}")

def publish_alert(context_message):
    mqtt_client.publish("sending/alert", context_message)
    print(f"Published alert: {context_message}")
    
sense = SenseHat()

R = (238, 37, 10) # Red colour
O = (238, 141, 10) # Orange colour
Y = (238, 210, 10) # Yellow colour
W = (255, 255, 255) # White colour
G =(9, 91, 11) # Green colour
L = (33, 232, 60 ) # Lime colour
B = (0,0,0) # Black colour (No colour)

mqtt_client = mqtt.Client()
broker_address = "localhost"
mqtt_client.connect(broker_address)

def save_data():
    user = "Default"
    temp = sense.get_temperature()
    calcTemp = 0.0071*temp*temp+0.86*temp-10.0
    gasDetect = 0;
    fireDetect = 1;
    current = datetime.now()
    currentMonth = current.month
    currentHour = current.hour
    currentDay = current.day
    currentYear = current.year
    light = calculate_sample_light(currentMonth,currentHour)
    humidity = sense.get_humidity()
    calcHum = humidity*(2.5-0.029*temp)
    pressure = sense.get_pressure()

    #sense.show_message ('%.0f %.1f %.0f' % (pressure, calctemp, calchum))
    data = {
        "user": user,
        "temp": round(calcTemp, 2),
        "gasDetect": gasDetect,
        "fireDetect": fireDetect,
        "light": light,
        "humidity": round(calcHum, 2),
        "pressure": round(pressure, 2),
        "month": currentMonth,
        "hour": currentHour,
        "day": currentDay,
        "year": currentYear
    }
    
    alert = "None"
    
    if fireDetect and gasDetect:
        alert = "Both"
    elif fireDetect:
        alert = "Fire"
    elif gasDetect:
        alert = "Gas"
    
    
    jsonData = json.dumps(data)
    #print(data)
    return jsonData, alert


def main():
    try:
        while True:
            dataInfo, alert = save_data()
            publish_context(dataInfo)
            if alert != "None":
                publish_alert(alert)
                if alert == "Fire":
                    fire_animation()
                elif alert == "Gas":
                    gas_animation()
                else:
                    fire_animation()
                    gas_animation()
            time.sleep(900)
    except KeyboardInterrupt:
        sense.clear()
        print("Bye bye")
        
if __name__ == "__main__":
    main()