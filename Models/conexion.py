import mysql.connector
import json

with open('Models/conexion.json', 'r') as f:
        data = json.load(f)
data_val = list(data.values())

def myDB():
      
    connect = mysql.connector.connect(
            host = data_val[0],
            user = data_val[1],
            password = data_val[2],
            database = data_val[3]
    )
    return connect


