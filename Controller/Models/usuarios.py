import mysql.connector
from Models.conexion import myDB

def showallusers():
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM usuarios")
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
    
def saveMedico(id, nombre, correo, dui, cargo, user, password):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
 
        if id != "" and dui != "" and nombre != "" and cargo != ""and user != "" and password != "":
            cursor.execute("INSERT INTO `medico` (`idMedico`, `especialidad`, `nombre`, `telefono`, `email`, `fechaNacimiento`, `sexo`) VALUES (?, ?, ?, ?, ?, ?, ?));",(id, nombre, correo, dui, cargo, user, password))
            mydb.commit()
            mydb.close()
            msg = "success"
            return msg
        else:
            msg = "failure"
            return msg
    except Exception as Error:
        print(Error)
        msg = "failure"
        return msg