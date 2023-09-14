import mysql.connector

def myDB():
    connect = mysql.connector.connect(
            host='localhost',
            user="root",
            password="",
            database="storage_db"
    )
    return connect

