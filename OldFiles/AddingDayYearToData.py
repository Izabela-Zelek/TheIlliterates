import pymysql
import random

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

cursor.execute("SELECT id, month FROM home")  
rows = cursor.fetchall()

def get_days_in_month(month, year):
    month_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    if month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return 29  
    return month_days.get(month, 31)  

for row in rows:
    id, month = row
    if month == 12:
        year = random.choice([2020, 2021, 2022, 2023]) 
    else:
        year = random.choice([2020, 2021, 2022, 2023, 2024])
    
    max_day = get_days_in_month(month, year)
    
    day = random.randint(1, max_day)
    
    cursor.execute("UPDATE home SET day = %s, year = %s WHERE id = %s", (day, year, id))

connection.commit()
cursor.close()
connection.close()