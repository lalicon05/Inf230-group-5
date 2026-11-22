import json
import mariadb

# Connect to mariadb database
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

cur = conn.cursor(dictionary=True)

cur.execute("SELECT VERSION()")
print(cur.fetchone())


# get all from physicalThing
cur.execute("select * from physicalThing")
things = cur.fetchall()

# get all from measurements
cur.execute("select * from measurements")
mes = cur.fetchall()

# get owners for measurements
cur.execute("""
    select h.measurement_id, p.physical_thing_title as thing
    from hasMeasurement h
    join PhysicalThing p on h.physical_thing_id = p.physical_thing_id

    """)
owner = {r["measurement_id"]: r["thing"] for r in cur.fetchall()}

#print(things)
#print(mes)

# context gotten from pC3.jsonld, changec to 'e' from 'c'
context = {
        "e": "https://home.bawue.de/~horsch/teaching/inf230/lab/inf230-oppgaave-E.html#",
        "xs": "http://www.w3.org/2001/XMLSchema#",
        "Name": { "@id": "e:Name", "@language": "en" },
        "HasMeasurement": { "@id": "e:HasMeasurement", "@type": "@id" },
        "MeasurementOf": { "@id": "e:MeasurementOf", "@type": "@id" },
        "SIUnit": "e:SIUnit",
        "MeasuredValue": { "@id": "e:MeasuredValue", "@type": "xs:float" },
        "MinimumValue": { "@id": "e:MinimumValue", "@type": "xs:float" },
        "MaximumValue": { "@id": "e:MaximumValue", "@type": "xs:float" },
        "UncertaintyAbsolute": { "@id": "e:UncertaintyAbsolute", "@type": "xs:float" },
        "UncertaintyPercent": { "@id": "e:UncertaintyPercent", "@type": "xs:float" },
        "ErrorAbsolute": { "@id": "e:ErrorAbsolute", "@type": "xs:float" },
        "ErrorPercent": { "@id": "e:ErrorPercent", "@type": "xs:float" }
    }

json_dict = {}
json_dict["@context"] = context

SI = {
    "is_length": ("Length", "m"),
    "is_mass": ("Mass", "kg"),
    "is_time": ("Time", "s"),
    "is_ElectricCurrent": ("ElectricCurrent", "A"),
    "is_temperature": ("Temperature", "K"),
    "is_mol": ("AmountOfSubstance", "mol")
}

graph = []
