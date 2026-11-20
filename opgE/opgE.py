import rdflib
import mariadb
import sys

try:
    conn = mariadb.connect(
        user="group5",
        password="group5",
        host="localhost",
        port=3306,
        database="inf230E"
    )
    print("Connected to database")

except mariadb.Error as e:
    print(f"Error: {e}")
    sys.exit(1)


"""
measurements = pd.read_csv("opgE/measurements.csv")
hasMeasurement = pd.read_csv("opgE/hasMeasurement.csv")
PhysicalThing = pd.read_csv("opgE/PhysicalThing.csv")

print(measurements.iloc[0].astype(str).tolist())
"""

cur = conn.cursor()

cur.execute("SELECT VERSION()")
print(cur.fetchone())

# Drop tables if they exist
cur.execute("""
    drop table if exists hasMeasurement;
    """)
cur.execute("""
    drop table if exists PhysicalThing;
    """)
cur.execute("""
    drop table if exists measurements;
    """)

# Create measurements tables
cur.execute("""
    create table measurements(
        measurement_id smallint,
        measurement_title varchar(32),
        MeasuredValue float,
        UncertaintyAbsolute float,
        ErrorAbsolute float,
        is_SI bool,
        is_length bool,
        is_mass bool,
        is_time bool,
        is_ElectricCurrent bool,
        is_temperature bool,
        is_mol bool,

        primary key(measurement_id)
    )
    """)

# Create physical thing table
cur.execute("""
    create table PhysicalThing(
        physical_thing_id smallint,
        physical_thing_title varchar(32),
        primary key(physical_thing_id)
    )
    """)

# create hasMeasurement table
cur.execute("""
    create table hasMeasurement(
        measurement_id smallint,
        physical_thing_id smallint,
        primary key(measurement_id, physical_thing_id),
        
        foreign key(measurement_id) references measurements,
        foreign key(physical_thing_id) references PhysicalThing
    )
    """)

# add to measurements table
rows = []

with open("opgE/measurements.csv", 'r') as file:
    file.readline()
    lines = file.readlines()
    for line in lines:
        line = line.strip().split(',')
        row = "("
        for item in line[:-1]:
            row += f'{item}, '
        row += f'{line[-1]})'
        rows.append(row)

for row in rows:
    cur.execute(f"insert into measurements values {row};")
    print(f"Inserted {row} into measurements")



print("inserted rows into measurements")

conn.commit() # <---------------- This god damn line
