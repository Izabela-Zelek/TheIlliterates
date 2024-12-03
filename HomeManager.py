import pymysql
import paho.mqtt.client as mqtt
import json
import smtplib
from email.message import EmailMessage
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request
import threading

from_email_addr ="theilliteratespi@gmail.com"
from_email_pass ="dlhp fcho dqnm ehds"
to_email_addr ="immatureluna@gmail.com"

db_name = "homemanager"
db_host = "localhost"
db_username = "admin"
db_password = "raspberrypi"

app = Flask(__name__)

def get_db():
    connection = pymysql.connect(host = db_host,
                           port = int(3306),
                           user = "root",
                           password = db_password,
                           db = db_name)
    return connection
    
    
def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
    client.subscribe("sending/sensorData")
    client.subscribe("sending/alert")
    
    
def on_message(client, userdata, msg):
    if msg.topic == "sending/sensorData":
        connection = get_db()
        cursor = connection.cursor()
        context_message = json.loads(msg.payload.decode())
        values = (context_message["user"], context_message["temp"], context_message["gasDetect"], context_message["fireDetect"], context_message["light"], context_message["humidity"], context_message["pressure"], context_message["month"], context_message["hour"], context_message["day"], context_message["year"])
        insert_query = """
        INSERT INTO home (user, temp, gasDetect, fireDetect, lightLevel, humidity, pressure, month, hour, day, year) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, values)
        connection.commit()
        print(f"Inserted {cursor.rowcount} row(s) into the database.")
        #print(f"Received context: {context_message}")
        cursor.close()
        connection.close()
    elif msg.topic == "sending/alert":
        connection = get_db()
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
        server.starttls() #Sends securely with tls
        server.login(from_email_addr, from_email_pass)
        server.send_message(msg)
        server.quit()
        connection.close()
    
    
@app.route('/dashboardJohn')
def dashJohn():
    connection = get_db()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    #Used in graphs to show in ascending order
    ascquery = "SELECT * FROM home ORDER BY year, month, day, hour"
    cursor.execute(ascquery)
    fullData = cursor.fetchall()
    monthly_averages = calculate_monthly_averages(fullData)
    
    #Used to fetch
    recentquery = "SELECT * FROM home ORDER BY year DESC, month DESC, day DESC, hour DESC"
    cursor.execute(recentquery)
    recent = cursor.fetchall()
    
    if recent:
        first_entry = recent[0]  
        recent = first_entry
    else:
        recent = None  
    
    #Only grabs data with alerts
    alertquery = "SELECT * FROM home WHERE fireDetect = 1 OR gasDetect = 1 ORDER BY year DESC, month DESC, day DESC, hour DESC"
    cursor.execute(alertquery)
    alerts = cursor.fetchall()
    
    today = datetime.today()
    current_year = 2024
    current_month = 11
    current_day = 30
    
    #Grabs data from specific day
    generalquery = "SELECT * FROM home WHERE year = %s AND month = %s AND day = %s ORDER BY year DESC, month DESC, day DESC, hour DESC"
    cursor.execute(generalquery, (current_year, current_month, current_day))
    general = cursor.fetchall()    
    cursor.close()
    connection.close()
    return render_template('index.html', alerts = alerts, recent = recent, general = general, monthly_averages = monthly_averages)


@app.route('/dataJohn')
def dataJohn():
    page = int(request.args.get('page', 1)) 
    DataPerPage = 100
    offset = (page - 1) * DataPerPage
    
    connection = get_db()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    recentquery = "SELECT * FROM home ORDER BY year DESC, month DESC, day DESC, hour DESC"
    cursor.execute(recentquery)
    recent = cursor.fetchall()
    
    if recent:
        first_entry = recent[0]  
        recent = first_entry
    else:
        recent = None
        
    #Grabs a limited amount of data for specific user, used to lessen load on webapp
    generalquery = "SELECT * FROM home WHERE user = %s ORDER BY year DESC, month DESC, day DESC, hour DESC LIMIT %s OFFSET %s"
    cursor.execute(generalquery, ("John", DataPerPage, offset))
    general = cursor.fetchall()
    
    #Grabs data from specific user
    count_query = "SELECT COUNT(*) as total FROM home WHERE user = %s"
    cursor.execute(count_query, ("John"))
    totalData = cursor.fetchone()['total']
    
    cursor.close()
    connection.close()
    return render_template('data.html', recent = recent, general = general, page=page, total_pages=(totalData + DataPerPage - 1) // DataPerPage)


@app.route('/dashboardJane')
def dashJane():
    connection = get_db()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    ascquery = "SELECT * FROM home ORDER BY year, month, day, hour"
    cursor.execute(ascquery)
    fullData = cursor.fetchall()
    monthly_averages = calculate_monthly_averages(fullData)
    
    recentquery = "SELECT * FROM home ORDER BY year DESC, month DESC, day DESC, hour DESC"
    cursor.execute(recentquery)
    recent = cursor.fetchall()
    
    if recent:
        first_entry = recent[0]  
        recent = first_entry
    else:
        recent = None  
    
    alertquery = "SELECT * FROM home WHERE fireDetect = 1 OR gasDetect = 1 ORDER BY year DESC, month DESC, day DESC, hour DESC"
    cursor.execute(alertquery)
    alerts = cursor.fetchall()
    
    today = datetime.today()
    current_year = 2024
    current_month = 11
    current_day = 30
    
    generalquery = "SELECT * FROM home WHERE year = %s AND month = %s AND day = %s ORDER BY year DESC, month DESC, day DESC, hour DESC"
    cursor.execute(generalquery, (current_year, current_month, current_day))
    general = cursor.fetchall()    
    cursor.close()
    connection.close()
    return render_template('indexJane.html', alerts = alerts, recent = recent, general = general, monthly_averages = monthly_averages)


@app.route('/dataJane')
def dataJane():
    page = int(request.args.get('page', 1)) 
    DataPerPage = 100
    offset = (page - 1) * DataPerPage
    
    connection = get_db()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    recentquery = "SELECT * FROM home ORDER BY year DESC, month DESC, day DESC, hour DESC"
    cursor.execute(recentquery)
    recent = cursor.fetchall()
    
    if recent:
        first_entry = recent[0]  
        recent = first_entry
    else:
        recent = None
        
    generalquery = "SELECT * FROM home WHERE user = %s ORDER BY year DESC, month DESC, day DESC, hour DESC LIMIT %s OFFSET %s"
    cursor.execute(generalquery, ("Jane", DataPerPage, offset))
    general = cursor.fetchall()
    
    count_query = "SELECT COUNT(*) as total FROM home WHERE user = %s"
    cursor.execute(count_query, ("Jane"))
    totalData = cursor.fetchone()['total']
    
    cursor.close()
    connection.close()
    return render_template('dataJane.html', recent = recent, general = general, page=page, total_pages=(totalData + DataPerPage - 1) // DataPerPage)


@app.route('/')
def index():
    return redirect(url_for('dashJohn'))

#Calculates average values for each month and year
def calculate_monthly_averages(data):
    monthly_data = {} #Defines a dictionary

    for entry in data:
        year = entry.get('year')
        month = entry.get('month')

        
        if year not in monthly_data:
            monthly_data[year] = {}
        if month not in monthly_data[year]:
            monthly_data[year][month] = {
                'temp': [],
                'humidity': [],
                'pressure': [],
                'lightLevel': []
            }
        monthly_data[year][month]['temp'].append(entry['temp'])
        monthly_data[year][month]['humidity'].append(entry['humidity'])
        monthly_data[year][month]['pressure'].append(entry['pressure'])
        monthly_data[year][month]['lightLevel'].append(entry['lightLevel'])
        
    #With the help of ChatGPT as was confused on how to handle work with dictionaries       
    averages = []
    for year, months in monthly_data.items():
        for month, values in months.items():
            averages.append({
                'year': year,
                'month': month,
                'temp': sum(values['temp']) / len(values['temp']) if values['temp'] else 0,
                'humidity': sum(values['humidity']) / len(values['humidity']) if values['humidity'] else 0,
                'pressure': sum(values['pressure']) / len(values['pressure']) if values['pressure'] else 0,
                'lightLevel': sum(values['lightLevel']) / len(values['lightLevel']) if values['lightLevel'] else 0,
            })

    return averages


def mqtt_client():
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    broker_address = "localhost"
    mqtt_client.connect(broker_address)
    mqtt_client.loop_forever()
    
    
def flask_app():
    app.run(debug=True, host='0.0.0.0')

#Starts mqtt on separate thread to avoid mqtt and flask clashing
def main():
    mqtt_thread = threading.Thread(target=mqtt_client)
    mqtt_thread.daemon = True
    mqtt_thread.start()
    
    flask_app()


if __name__ == '__main__':
    main()
    