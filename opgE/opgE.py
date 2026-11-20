import rdflib
import pymysql

sql = pymysql.connect(user='group5', password='group5')
sql.query(sql='drop database if exists INF230E;')
sql.query(sql='create database INF230E;')
sql.query(sql='use INF230E;')
