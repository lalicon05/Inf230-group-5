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

cur.close()
db.close()
