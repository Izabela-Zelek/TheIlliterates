import pymysql
import paho.mqtt.client as mqtt
import json
import smtplib
from email.message import EmailMessage
from datetime import datetime

def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
    client.subscribe("sending/sensorData")
    client.subscribe("sending/alert")
    
def on_message(client, userdata, msg):
    if msg.topic == "sending/sensorData":
        cursor = connection.cursor()
        context_message = json.loads(msg.payload.decode())
        values = (context_message["user"], context_message["temp"], context_message["gasDetect"], context_message["fireDetect"], context_message["light"], context_message["humidity"], context_message["pressure"], context_message["month"], context_message["hour"], context_message["day"], context_message["year"])
        #cursor.execute(insert_query, values)
        #connection.commit()
        #print(f"Inserted {cursor.rowcount} row(s) into the database.")
        #print(f"Received context: {context_message}")
        cursor.close()
    elif msg.topic == "sending/alert":
        message = msg.payload.decode()
        msg = EmailMessage()
        msg['From'] = from_email_addr
        msg['To'] = to_email_addr
        body = "Null"
        time = datetime.now()
        if message == "Fire":
            msg['Subject'] = 'Fire Alert'
            body = f"Fire detected at {time.strftime('%H:%M')} on {time.strftime('%d/%m/%y')}"
        elif message == "Gas":
            msg['Subject'] = 'Gas Alert'
            body = f"Gas detected at {time.strftime('%H:%M')} on {time.strftime('%d/%m/%y')}"
        else:
            msg['Subject'] = 'Fire and Gas Alert'
            body = f"Fire and Gas detected at {time.strftime('%H:%M')} on {time.strftime('%d/%m/%y')}"
        msg.set_content(body)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email_addr, from_email_pass)
        server.send_message(msg)
        server.quit()
        
from_email_addr ="theilliteratespi@gmail.com"
from_email_pass ="dlhp fcho dqnm ehds"
to_email_addr ="immatureluna@gmail.com"

db_name = "homemanager"
db_host = "localhost"
db_username = "admin"
db_password = "raspberrypi"

connection = pymysql.connect(host = db_host,
                           port = int(3306),
                           user = "root",
                           password = db_password,
                           db = db_name)


insert_query = """
INSERT INTO home (user, temp, gasDetect, fireDetect, lightLevel, humidity, pressure, month, hour, day, year) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
broker_address = "localhost"
mqtt_client.connect(broker_address)
mqtt_client.loop_forever()
connection.close()

    
