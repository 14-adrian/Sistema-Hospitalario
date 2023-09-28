import mysql.connector

def myDB():
    connect = mysql.connector.connect(
            host='localhost',
            user="root",
            password="",
            database="hospital_db"
    )
    return connect

