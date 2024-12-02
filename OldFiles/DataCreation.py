import pymysql
from datetime import datetime
import random
import pandas as pd

#mariadb -u root -p -h localhost

#Select database
#USE homemanager;

#Shows structure of table
#DESCRIBE home;

#removes all data
#TRUNCATE TABLE home;

# Order by month and hour, shows 20 top
#SELECT * FROM home ORDER BY year, month, day, hour LIMIT 20;

#Display nr of rows
#SELECT COUNT(*) from home;

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
INSERT INTO home (user, temp, gasDetect, fireDetect, lightLevel, month, hour) 
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

dataLimit = 3000
user1Data = 3000
user2Data = 3000
user = ""
temp = 0
gasDetect = 0;
fireDetect = 0;
lightLevel = 0;
month = 0;
hour = 0;
next_row = 0;

df = pd.read_csv("Dataset.csv")

while user1Data < dataLimit and user2Data < dataLimit:
    number = random.randint(0, 2)
    if number == 0:
        user = "John"
        season = random.randint(0, 3)
        if season == 0:
            month = random.randint(2,4)
            hour = random.randint(0,23)
            if 8 <= hour <= 15:
                temp = round(random.uniform(7, 10), 2)
                lightLevel = 0
                gasDetect = 0
                fireDetect = 0
            elif 16 <= hour <= 18:
                temp = round(random.uniform(18, 22), 2)
                lightLevel = random.randint(0, 300)
                gasDetect = 0
                fireDetect = 0
            elif 19 <= hour <= 22:
                temp = round(random.uniform(18, 22), 2)
                lightLevel = random.randint(300, 600)
                gasDetect = 0
                fireDetect = 0
            else:
                temp = round(random.uniform(12, 16), 2)
                lightLevel = 0
                gasDetect = 0
                fireDetect = 0
        elif season == 1:
            month = random.randint(5,7)
            hour = random.randint(0,23)
            if 8 <= hour <= 21:
                temp = round(random.uniform(13, 16), 2)
                lightLevel = 0
                gasDetect = 0
                fireDetect = 0
            elif 0 <= hour <= 7:
                temp = round(random.uniform(13, 16), 2)
                lightLevel = 0
                gasDetect = 0
                fireDetect = 0
            else:
                temp = round(random.uniform(13, 16), 2)
                lightLevel = 0
                gasDetect = 0
                fireDetect = 0
        elif season == 2:
            month = random.randint(8,10)
            hour = random.randint(0,23)
            if 8 <= hour <= 15:
                temp = round(random.uniform(11, 16), 2)
                lightLevel = 0
                gasDetect = 0
                fireDetect = 0
            elif 16 <= hour <= 20:
                temp = round(random.uniform(13, 18), 2)
                lightLevel = random.randint(0, 300)
                gasDetect = 0
                fireDetect = 0
            elif 21 <= hour <= 22:
                temp = round(random.uniform(15, 20), 2)
                lightLevel = random.randint(300, 600)
                gasDetect = 0
                fireDetect = 0
            else:
                temp = round(random.uniform(11, 16), 2)
                lightLevel = 0
                gasDetect = 0
                fireDetect = 0
        else:
            month = random.choice([11, 12, 1])
            hour = random.randint(0,23)
            if 8 <= hour <= 15:
                temp = round(random.uniform(2, 8), 2)
                lightLevel = 0
                gasDetect = 0
                fireDetect = 0
            elif 16 <= hour <= 17:
                temp = round(random.uniform(11, 16), 2)
                lightLevel = random.randint(0, 300)
                gasDetect = 0
                fireDetect = 0
            elif 18 <= hour <= 22:
                temp = round(random.uniform(15, 20), 2)
                lightLevel = random.randint(300, 600)
                gasDetect = 0
                fireDetect = 0
            else:
                temp = round(random.uniform(5, 12), 2)
                lightLevel = random.randint(0, 300)
                gasDetect = 0
                fireDetect = 0
        user1Data = user1Data + 1
    elif number == 1:
        user = "Jane"
        season = random.randint(0, 3)
        if season == 0:
            month = random.randint(2,4)
            hour = random.randint(0,23)
            if 8 <= hour <= 15:
                temp = round(random.uniform(10, 14), 2)
                lightLevel = random.randint(0, 300)
                gasDetect = 0
                fireDetect = 0
            elif 16 <= hour <= 19:
                temp = round(random.uniform(12, 16), 2)
                lightLevel = random.randint(300, 600)
                gasDetect = 0
                fireDetect = 0
            elif 20 <= hour <= 22:
                temp = round(random.uniform(18, 22), 2)
                lightLevel = random.randint(300, 600)
                gasDetect = 0
                fireDetect = 0
            else:
                temp = round(random.uniform(16, 18), 2)
                lightLevel = random.randint(0, 300)
                gasDetect = 0
                fireDetect = 0
        elif season == 1:
            month = random.randint(5,7)
            hour = random.randint(0,23)
            if 8 <= hour <= 21:
                temp = round(random.uniform(11, 14), 2)
                lightLevel = 0
                gasDetect = 0
                fireDetect = 0
            elif 0 <= hour <= 7:
                temp = round(random.uniform(13, 16), 2)
                lightLevel = 0
                gasDetect = 0
                fireDetect = 0
            else:
                temp = round(random.uniform(11, 14), 2)
                lightLevel = random.randint(300, 600)
                gasDetect = 0
                fireDetect = 0
        elif season == 2:
            month = random.randint(8,10)
            hour = random.randint(0,23)
            if 8 <= hour <= 15:
                temp = round(random.uniform(11, 16), 2)
                lightLevel = 0
                gasDetect = 0
                fireDetect = 0
            elif 16 <= hour <= 20:
                temp = round(random.uniform(13, 18), 2)
                lightLevel = random.randint(0, 300)
                gasDetect = 0
                fireDetect = 0
            elif 21 <= hour <= 22:
                temp = round(random.uniform(15, 20), 2)
                lightLevel = random.randint(300, 600)
                gasDetect = 0
                fireDetect = 0
            else:
                temp = round(random.uniform(14, 18), 2)
                lightLevel = 0
                gasDetect = 0
                fireDetect = 0
        else:
            month = random.choice([11, 12, 1])
            hour = random.randint(0,23)
            if 8 <= hour <= 15:
                temp = round(random.uniform(11, 16), 2)
                lightLevel = random.randint(0, 300)
                gasDetect = 0
                fireDetect = 0
            elif 16 <= hour <= 17:
                temp = round(random.uniform(13, 18), 2)
                lightLevel = random.randint(0, 300)
                gasDetect = 0
                fireDetect = 0
            elif 18 <= hour <= 22:
                temp = round(random.uniform(13, 16), 2)
                lightLevel = random.randint(300, 600)
                gasDetect = 0
                fireDetect = 0
            else:
                temp = round(random.uniform(10, 12), 2)
                lightLevel = random.randint(0, 300)
                gasDetect = 0
                fireDetect = 0
        user2Data = user2Data + 1
    elif number == 2:
        if next_row < len(df):
            row = df.iloc[next_row]
            user = "Default"
            temp = float(row['Temperature'])
            lightLevel = int(row['LightIntensity'])
            gasDetect = int(row['GasDetect'])
            fireDetect = int(row['FireDetect'])
            month = int(row['Month'])
            hour = int(row['Hour_of_Day'])
            next_row = next_row + 1
    data = (user, temp, gasDetect, fireDetect, lightLevel, month, hour)
    cursor.execute(insert_query, data)



connection.commit()

print(f"Inserted {cursor.rowcount} row(s) into the database.")

query = "SELECT * FROM home ORDER BY year DESC, month DESC, day DESC, hour DESC"

all_data_df = pd.read_sql(query, connection)

all_data_df.to_csv('fullData.csv', index=False)

cursor.close()
connection.close()