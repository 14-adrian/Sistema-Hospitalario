import mysql.connector
from Models.conexion import myDB

def showallmedicos():
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM medico")
        registers = []
        for item in cursor.fetchall():
            #test = item[1]
            #print(test)
            registers.append(item)
        
        return registers
    except Exception as error:
        print(error)
        msg = "Error"
        return msg