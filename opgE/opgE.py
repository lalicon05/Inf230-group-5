import csv
import json
from pathlib import Path

import mariadb

BASE = Path(__file__).parent
db = mariadb.connect(host="localhost", user="group5", password="group5")
cur = db.cursor()


cur.execute("drop database if exists inf230e")
cur.execute("create database inf230e")
cur.execute("use inf230e")

cur.execute("""
create table PhysicalThing (
    physical_thing_id smallint primary key,
    physical_thing_title varchar(32)
)""")
cur.execute("""
create table measurements (
    measurement_id smallint primary key,
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
    is_mol bool
)""")
cur.execute("""
create table hasMeasurement (
    measurement_id smallint,
    physical_thing_id smallint,
    primary key (measurement_id, physical_thing_id),
    foreign key (measurement_id) references measurements(measurement_id),
    foreign key (physical_thing_id) references PhysicalThing(physical_thing_id)
)""")


def rows(name):
    with (BASE / name).open(newline="", encoding="utf-8") as f:
        return [
            {k: v.strip().strip("'").strip('"') for k, v in row.items()}
            for row in csv.DictReader(f)
        ]


for r in rows("PhysicalThing.csv"):
    cur.execute(
        "insert into PhysicalThing values (?,?)",
        (int(r["physical_thing_id"]), r["physical_thing_title"]),
    )

for r in rows("measurements.csv"):
    cur.execute(
        "insert into measurements values (?,?,?,?,?,?,?,?,?,?,?,?)",
        (
            int(r["measurement_id"]),
            r["measurement_title"],
            *(
                float(r[k])
                for k in ("MeasuredValue", "UncertaintyAbsolute", "ErrorAbsolute")
            ),
            *(
                r[k].lower() == "true"
                for k in (
                    "is_SI",
                    "is_length",
                    "is_mass",
                    "is_time",
                    "is_ElectricCurrent",
                    "is_temperature",
                    "is_mol",
                )
            ),
        ),
    )

for r in rows("hasMeasurement.csv"):
    cur.execute(
        "insert into hasMeasurement values (?,?)",
        (int(r["measurement_id"]), int(r["physical_thing_id"])),
    )

db.commit()

print("Database inf230e created and CSV data inserted successfully.")
for table in ("PhysicalThing", "measurements", "hasMeasurement"):
    cur.execute(f"select count(*) from {table}")
    print(f"{table}: {cur.fetchone()[0]} rows")

cur.execute("""
select
    p.physical_thing_id,
    p.physical_thing_title,
    m.measurement_id,
    m.measurement_title,
    m.MeasuredValue,
    m.UncertaintyAbsolute,
    m.ErrorAbsolute
from PhysicalThing p
join hasMeasurement h on h.physical_thing_id = p.physical_thing_id
join measurements m on m.measurement_id = h.measurement_id
order by p.physical_thing_id, m.measurement_id
""")
print("\nStored measurements:")
for row in cur:
    print(row)

cur.close()
db.close()
