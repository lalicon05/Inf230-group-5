import rdflib
import mariadb
import sys


def get_rows(filepath: str) -> list:
    """
    Processes a CSV file and returns a list of strings
    where the strings are the rows of the CSV file
    given in a SQL friendly syntax for\n
    INSERT INTO *table* VALUES *row*

    :param filepath: String of the relative path of the CSV file
    """
    rows = []  # List of SQL friendly value strings
    with open(filepath, 'r') as file:
        file.readline()  # Header
        lines = file.readlines()
        # Goes through each line in the CSV file
        # Builds a string of each line in the format
        # (val1, val2, val3, ..., valn)
        for line in lines:
            line = line.strip().split(',')
            row = "("
            for item in line[:-1]:
                row += f'{item}, '
            row += f'{line[-1]})'
            rows.append(row)
    return rows


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

measurements = get_rows('opgE/measurements.csv')
hasMeasurement = get_rows('opgE/hasMeasurement.csv')
PhysicalThing = get_rows('opgE/PhysicalThing.csv')

for row in measurements:
    cur.execute(f"insert into measurements values {row};")
    print(f"Inserted {row} into measurements")

for row in PhysicalThing:
    cur.execute(f"insert into PhysicalThing values {row};")
    print(f"Inserted {row} into PhysicalThing")

for row in hasMeasurement:
    cur.execute(f"insert into hasMeasurement values {row};")
    print(f"Inserted {row} into hasMeasurement")

print("inserted rows into measurements")

conn.commit() # <---------------- This god damn line
conn.close()
