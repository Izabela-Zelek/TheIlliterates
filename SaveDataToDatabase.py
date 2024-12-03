import pymysql
import csv

def import_csv_to_table(host, user, password, database, table_name, input_file):
    try:
        # Connect to the database
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = connection.cursor()
        
        # Open the CSV file
        with open(input_file, mode='r') as file:
            reader = csv.reader(file)
            columns = next(reader)  # Get column headers
            
            # Construct SQL query
            placeholders = ', '.join(['%s'] * len(columns))
            query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
            
            # Insert data
            for row in reader:
                cursor.execute(query, row)
        
        connection.commit()
        print(f"Data imported successfully from {input_file}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()

# Example usage
import_csv_to_table(
    host="localhost",
    user="admin",
    password="raspberrypi",
    database="homemanager",
    table_name="test",
    input_file="AllDatabaseData.csv"
)
