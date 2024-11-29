from flask import Flask, render_template
import pymysql
from datetime import datetime
app = Flask(__name__)

db_name = "homemanager"
db_host = "localhost"
db_username = "admin"
db_password = "raspberrypi"

def get_db():
    connection = pymysql.connect(host = db_host,
                           port = int(3306),
                           user = "root",
                           password = db_password,
                           db = db_name)
    return connection

@app.route('/')
def index():
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
    
    alertquery = "SELECT * FROM home ORDER BY year DESC, month DESC, day DESC, hour DESC"
    cursor.execute(alertquery)
    alerts = cursor.fetchall()
    
    today = datetime.today()
    current_year = 2024
    current_month = 11
    current_day = 30
    
    
    generalquery = "SELECT * FROM home WHERE year = %s AND month = %s AND day = %s ORDER BY year DESC, month DESC, day DESC, hour DESC"
    cursor.execute(generalquery, (current_year, current_month, current_day))
    general = cursor.fetchall()
    
    connection.close()
    
    return render_template('index.html', alerts = alerts, recent = recent, general = general)

@app.route('/data')
def data():
    
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
        
    generalquery = "SELECT * FROM home ORDER BY year DESC, month DESC, day DESC, hour DESC"
    cursor.execute(generalquery)
    general = cursor.fetchall()
    
    connection.close()
    return render_template('data.html', recent = recent, general = general)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')