import pymysql
from datetime import datetime

db_name = "homemanager"
db_host = "localhost"
db_username = "admin"
db_password = "raspberrypi"

connection = pymysql.connect(host = db_host,
                           port = int(3306),
                           user = "root",
                           password = db_password,
                           db = db_name)

cursor = connection.cursor()

insert_query = """
INSERT INTO home (user, temp, humidity, gasDetect, fireDetect, lightLevel, timestamp) 
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

timestamp = datetime.now()

data = ("John Doe", 38.14, 32.10, 0, 0, 480, timestamp)

cursor.execute(insert_query, data)

connection.commit()

print(f"Inserted {cursor.rowcount} row(s) into the database.")

cursor.close()
connection.close()