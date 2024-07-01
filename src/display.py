import sqlite3 as connector

# Define database file path
db_path = "database/my_dbase.db"

def display_data():
    try:
        # Connect to the database
        conn = connector.connect(db_path)
        conn.execute("PRAGMA foreign_keys = on")
        cursor = conn.cursor()

        # Query and display data from the municipality table
        print("Municipality Table:")
        cursor.execute("SELECT * FROM municipality")
        municipalities = cursor.fetchall()
        for row in municipalities:
            print(row)
        
        # Query and display data from the populacao table
        print("\nPopulation Table:")
        cursor.execute("SELECT * FROM populacao")
        populations = cursor.fetchall()
        for row in populations:
            print(row)
        
        # Query and display data from the dengue table
        print("\nDengue Cases Table:")
        cursor.execute("SELECT * FROM dengue")
        dengue_cases = cursor.fetchall()
        for row in dengue_cases:
            print(row)
        
    except connector.DatabaseError as e:
        print("Database Error:", e)
    except connector.OperationalError as e:
        print("Operational Error:", e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

display_data()
