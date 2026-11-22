import pymysql
import rdflib
import json


def get_dict(table: str):
    """
    Returns a dict of format
    column_name: [values]

    :param table: Table name
    """
    cur.execute(f'SELECT * FROM {table}')
    # Get column names
    cols = [col[0] for col in cur.description]
    rows = cur.fetchall()
    dict = {}
    # Build the key value pair for each column
    for i in range(len(cols)):
        dict[cols[i]] = []
        for row in rows:
            dict[cols[i]].append(row[i])
    return dict


conn = pymysql.connect(
    user='group5',
    password='group5',
    host='localhost',
    port=3306,
    database='inf230E'
)

cur = conn.cursor()

measurements = get_dict('measurements')
PhysicalThing = get_dict('PhysicalThing')
hasMeasurement = get_dict('hasMeasurement')

json_dict = {}

# Build context
context = {
    "e": "https://home.bawue.de/~horsch/teaching/inf230/lab/inf230-oppgaave-E.html#",
    "xs": "http://www.w3.org/2001/XMLSchema#",
    "Name": {
      "@id": "e:Name",
      "@language": "en"
    },
    "HasMeasurement": {
      "@id": "e:HasMeasurement",
      "@type": "@id"
    },
    "MeasurementOf": {
      "@id": "e:MeasurementOf",
      "@type": "@id"
    },
    "MeasuredValue": {
      "@id": "e:MeasuredValue",
      "@type": "xs:float"
    },
    "UncertaintyAbsolute": {
      "@id": "e:UncertaintyAbsolute",
      "@type": "xs:float"
    },
    "ErrorAbsolute": {
      "@id": "e:ErrorAbsolute",
      "@type": "xs:float"
    }
}

json_dict['@context'] = context

graph = []

# Build the PhysicalThing part of the graph
for i in range(len(PhysicalThing["physical_thing_id"])):
    # Create dict for this node
    graph.append({})
    node = graph[-1]

    # Add id, type and name
    node["@id"] = f"e:{PhysicalThing["physical_thing_title"][i]}"
    node["@type"] = "e:PhysicalThing"
    node["e:Name"] = PhysicalThing["physical_thing_title"][i]

    # Find what measurements have been done on the thing
    node["e:HasMeasurement"] = []
    thing_id = PhysicalThing["physical_thing_id"][i]
    cur.execute(f'SELECT measurement_id FROM hasMeasurement where physical_thing_id = {thing_id}')
    query = cur.fetchall()
    measurement_ids = []
    for row in query:
        measurement_ids.append(row[0])
    for id in measurement_ids:
        cur.execute(f'SELECT measurement_title FROM measurements WHERE measurement_id = {id}')
        query = cur.fetchall()
        for row in query:
            node["e:HasMeasurement"].append(f'e:{row[0]}')

# Build the measurements part of the graph
for i in range(len(measurements["measurement_id"])):
    # Create dict for this node
    graph.append({})
    node = graph[-1]

    # Add the id of measurement
    node["@id"] = f'e:{measurements['measurement_title'][i]}'

    # Find the SI unit type
    if measurements['is_length'][i]:
        node["@type"] = 'e:length'
    elif measurements['is_mass'][i]:
        node["@type"] = 'e:mass'
    elif measurements['is_time'][i]:
        node["@type"] = 'e:time'
    elif measurements['is_ElectricCurrent'][i]:
        node["@type"] = 'e:ElectricCurrent'
    elif measurements['is_temperature'][i]:
        node["@type"] = 'e:temperature'
    elif measurements['is_mol'][i]:
        node["@type"] = 'e:mol'

    # Add the name of measurement
    node['e:Name'] = measurements['measurement_title'][i]

    # Find the PhysicalThing title of what is being measured
    cur.execute(
        f'SELECT physical_thing_id FROM hasMeasurement where measurement_id = {
            measurements['measurement_id'][i]
            }'
        )
    query = cur.fetchall()
    physical_thing_id = query[0][0]
    cur.execute(
        f'SELECT physical_thing_title FROM PhysicalThing where physical_thing_id = {
            physical_thing_id
            }'
        )
    query = cur.fetchall()
    thing_title = query[0][0]
    node["e:MeasurementOf"] = thing_title

    # Number values of measurement
    node["e:MeasuredValue"] = measurements["MeasuredValue"][i]
    node["e:UncertaintyAbsolute"] = measurements["UncertaintyAbsolute"][i]
    node["e:ErrorAbsolute"] = measurements["ErrorAbsolute"][i]

json_dict["@graph"] = graph
json_str = json.dumps(json_dict, indent=4)
with open("opgE/pE.jsonld", "w") as file:
    file.write(json_str)

conn.close()
