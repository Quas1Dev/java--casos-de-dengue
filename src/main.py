import os
import sqlite3 as connector

# Define database file path
db_path = "database/my_dbase.db"

# Check if the database directory exists
db_dir = os.path.dirname(db_path)
if not os.path.exists(db_dir):
    os.makedirs(db_dir)

# Print current working directory
print("Current working directory:", os.getcwd())

conn = None 
cursor = None

try:
    # Establishing connection
    conn = connector.connect(db_path)
    # All our scripts consider the foreign keys restriction
    conn.execute("PRAGMA foreign_keys = on")
    cursor = conn.cursor()
    
    # Create municipality table
    command = """ 
    CREATE TABLE IF NOT EXISTS municipality (
        cod_municipality INTEGER NOT NULL,
        name VARCHAR(32) NOT NULL,
        PRIMARY KEY (cod_municipality)
    );
    """
    cursor.execute(command)

    # Create populacao table
    command = """ 
    CREATE TABLE IF NOT EXISTS populacao (
        cod_municipality INTEGER NOT NULL,
        year INTEGER NOT NULL,
        amount INTEGER NOT NULL,
        CONSTRAINT fk_municipality FOREIGN KEY (cod_municipality) REFERENCES municipality(cod_municipality),
        PRIMARY KEY (cod_municipality, year)
    );
    """
    cursor.execute(command)

    # Create dengue table
    command = """ 
    CREATE TABLE IF NOT EXISTS dengue (
        cod_municipality INTEGER NOT NULL,
        year INTEGER NOT NULL,
        cases INTEGER NOT NULL,
        CONSTRAINT fk_municipality FOREIGN KEY (cod_municipality) REFERENCES municipality(cod_municipality),
        PRIMARY KEY (cod_municipality, year)
    );
    """
    cursor.execute(command)

    conn.commit()

except connector.DatabaseError as e:
    print("Database Error:", e)
except connector.OperationalError as e:
    print("Operational Error:", e)
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()

# Re-establish connection for seeding data
try:
    conn = connector.connect(db_path)
    conn.execute("PRAGMA foreign_keys = on")
    cursor = conn.cursor()

    # Seed database from CSV file
    csv_file_path = 'data/casos-dengue.csv'
    if not os.path.isfile(csv_file_path):
        raise FileNotFoundError(f"The file {csv_file_path} does not exist.")

    with open(csv_file_path) as dengueFileData:
        # Read heading to move to the second line
        dengueFileData.readline()

        for line in dengueFileData:
            if line.strip().split(';')[0].isdigit():
                cod_municipality, name, cases2018, cases2019, total = line.strip().split(';')
                
                try:
                    cases2018 = int(cases2018) if cases2018.isdigit() else 0
                    cases2019 = int(cases2019) if cases2019.isdigit() else 0
                except ValueError:
                    print(f"Skipping row with invalid data: {line.strip()}")
                    continue
                
                # Insert into municipality table
                cursor.execute("INSERT OR IGNORE INTO municipality (cod_municipality, name) VALUES (?, ?)", 
                               (int(cod_municipality), name))
                
                # Insert into dengue table
                cursor.execute("INSERT OR IGNORE INTO dengue (cod_municipality, year, cases) VALUES (?, ?, ?)", 
                               (int(cod_municipality), 2018, cases2018))
                cursor.execute("INSERT OR IGNORE INTO dengue (cod_municipality, year, cases) VALUES (?, ?, ?)", 
                               (int(cod_municipality), 2019, cases2019))

    conn.commit()

except FileNotFoundError as e:
    print("File Error:", e)
except connector.DatabaseError as e:
    print("Database Error during seeding:", e)
except connector.OperationalError as e:
    print("Operational Error during seeding:", e)
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()


"""
Dev's comments

Calculate the anual incidence rate for Dangue in Rio de Janeiro
for the years of 2018 and 2019.

Incidence rate: new case rate / amount of people at risk

Steps:

- Create a database system to store cases of Dangue.
- Create ER model for the database.
- Seed database using Dengue and population data organized into spreadsheets.
- Query database to retrieve Dangue incidence.
"""


