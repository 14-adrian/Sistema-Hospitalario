import mysql.connector

def myDB():
    conect = mysql.connector.connect(
            host='localhost',
            user="root",
            password="",
            database="storage_db"
    )
    return conect

