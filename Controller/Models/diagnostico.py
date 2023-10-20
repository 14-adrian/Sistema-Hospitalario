import mysql.connector
from Models.conexion import myDB

def showalldiag():
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM diagnostico")
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
    
    
def saveDiag(id, nombreM, nombreP, tipo, fecha, estado):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        print(nombreM)
 
        if id != "" and nombreM != "" and nombreP != "" and tipo != ""and fecha != "" and estado != "":
            add_cita = """INSERT INTO `cita` (`idCita`, `Nombre Medico`, `Nombre Paciente`, `tipoConsulta`, `fechaSolicitud`, `estado`) 
            VALUES (%s, %s, %s, %s, %s, %s);"""
            data_cita = (id, nombreM, nombreP, tipo, fecha, estado)
            cursor.execute(add_cita, data_cita)
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
    
def showSelectedDiag(id):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        print(id)
        sel_cita = """ SELECT * FROM cita
                            WHERE `idCita` = %s;"""
        data_cita = (id,)
        cursor.execute(sel_cita, data_cita)
        editarcita = []
        for item in cursor.fetchone():
            editarcita.append(item)
        return editarcita
    except Exception as Error:
        print(Error)
        msg = "failure"
        return msg

def updateCita(id, nombreM, nombreP, tipo, fecha, estado):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        print(nombreM)
 
        if id != "" and nombreM != "" and nombreP != "" and tipo != ""and fecha != "" and estado != "":
            upd_cita = """UPDATE `cita` SET
              `Nombre Medico` = %s , `Nombre Paciente` = %s,
                `tipoConsulta` = %s, `fechaSolicitud` = %s,
                  `estado` = %s
            WHERE `cita`.`idCita` = %s;
            """
            data_cita = (nombreM, nombreP, tipo, fecha, estado, id)
            cursor.execute(upd_cita, data_cita)
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
    
def deleteCita(id):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        del_cita = """DELETE FROM cita
        WHERE `cita`.`idCita` = %s
            """
        data_cita = (id,)
        cursor.execute(del_cita, data_cita)
        mydb.commit()
        mydb.close()
        msg = "success"
        return msg
             
    except Exception as error:
        print(error)
        msg = "Error"
        return msg