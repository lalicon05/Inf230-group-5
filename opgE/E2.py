
import mariadb
import sys
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS, XSD

# Database connection
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

# Retrieve SQL data
cur.execute("SELECT * FROM measurements")
measurements = cur.fetchall()

cur.execute("SELECT * FROM PhysicalThing")
physical_things = cur.fetchall()

cur.execute("SELECT * FROM hasMeasurement")
relationships = cur.fetchall()

# Create RDF graph and namespaces
g = Graph()

C = Namespace("https://home.bawue.de/~horsch/teaching/inf230/lab/inf230-oppgaave-C.html#")
g.bind("c", C)

DATA = Namespace("https://home.bawue.de/~horsch/teaching/inf230/lab/data#")
g.bind("data", DATA)


# Create PhysicalThing instances
for row in physical_things:
    physical_thing_id = row[0]
    thing_title = row[1]

    thing = DATA[f"PhysicalThing{physical_thing_id}"]

    # Class
    g.add((thing, RDF.type, C.PhysicalThing))

    # Name
    g.add((
        thing,
        C.Name,
        Literal(thing_title, datatype=XSD.string)
    ))

    # label
    g.add((
        thing,
        RDFS.label,
        Literal(thing_title)
    ))



# SQL column index -> ontology class
measurement_types = {
    6: C.Length,
    7: C.Mass,
    8: C.Time,
    9: C.ElectricCurrent,
    10: C.Temperature,
    11: C.AmountOfSubstance
}

# Create Measurement instances
for row in measurements:
    measurement_id = row[0]
    measurement_title = row[1]

    measurement = DATA[f"Measurement{measurement_id}"]

    # Every measurement is a Measurement
    g.add((measurement, RDF.type, C.Measurement))

    # Measurement title
    g.add((
        measurement,
        RDFS.label,
        Literal(measurement_title)
    ))

    # MeasuredValue
    g.add((
        measurement,
        C.MeasuredValue,
        Literal(row[2], datatype=XSD.float)
    ))

    # UncertaintyAbsolute
    g.add((
        measurement,
        C.UncertaintyAbsolute,
        Literal(row[3], datatype=XSD.float)
    ))

    # ErrorAbsolute
    g.add((
        measurement,
        C.ErrorAbsolute,
        Literal(row[4], datatype=XSD.float)
    ))

    # Add SIMeasurement superclass if applicable
    if row[5]:
        g.add((measurement, RDF.type, C.SIMeasurement))

    # Determine specific measurement class
    for column, measurement_class in measurement_types.items():

        if row[column]:
            g.add((
                measurement,
                RDF.type,
                measurement_class
            ))


# Create relationships
for row in relationships:
    measurement_id = row[0]
    physical_thing_id = row[1]

    measurement = DATA[f"Measurement{measurement_id}"]
    thing = DATA[f"PhysicalThing{physical_thing_id}"]

    # PhysicalThing has a measurement
    g.add((
        thing,
        C.HasMeasurement,
        measurement
    ))

    # Measurement belongs to a physical thing
    g.add((
        measurement,
        C.MeasurementOf,
        thing
    ))

# Export JSON-LD
g.serialize(
    destination="E2_output.jsonld",
    format="json-ld",
    auto_compact=True
)

conn.close()