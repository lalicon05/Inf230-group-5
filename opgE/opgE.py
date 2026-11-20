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

cur.close()
db.close()
