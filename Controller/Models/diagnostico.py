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
    
def showNombreMD():
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        cursor.execute("SELECT `Nombre Medico` FROM cita")
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
    
def showNombrePD():
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        cursor.execute("SELECT `Nombre Paciente` FROM cita")
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
    
def showLstMed():
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        cursor.execute("SELECT Descripcion FROM medicina")
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
    
    
def saveDiag(id, paciente, medico, idc, desc, medicina):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        print(paciente)
 
        if id != "" and paciente != "" and medico != "" and idc != ""and desc != "" and medicina != "":
            add_diag = """INSERT INTO `diagnostico` 
            (`idDiagnostico`, `Paciente`, `Medico`, `id_Cita`, `descripcion`, `medicina`) 
            VALUES (%s, %s, %s, %s, %s, %s);"""
            data_diag = (id, paciente, medico, idc, desc, medicina)
            cursor.execute(add_diag, data_diag)
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
        sel_diag = """ SELECT * FROM `diagnostico`
                            WHERE `idDiagnostico` = %s;"""
        data_diag = (id,)
        cursor.execute(sel_diag, data_diag)
        editarcita = []
        for item in cursor.fetchone():
            editarcita.append(item)
        return editarcita
    except Exception as Error:
        print(Error)
        msg = "failure"
        return msg

def updateDiag(id, paciente, medico, idc, desc, medicina):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        print(paciente)
 
        if id != "" and paciente != "" and medico != "" and idc != ""and desc != "" and medicina != "":
            upd_diag = """UPDATE `diagnostico` 
            SET `Paciente` = %s,
              `Medico` = %s, `id_Cita` = %s,
                `descripcion` = %s, `medicina` = %s
            WHERE `diagnostico`.`idDiagnostico` = %s;
            """
            data_diag = (paciente, medico, idc, desc, medicina, id)
            cursor.execute(upd_diag, data_diag)
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
    
def deleteDiag(id):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        del_diag = """DELETE FROM diagnostico 
        WHERE `diagnostico`.`idDiagnostico` = %s
            """
        data_diag = (id,)
        cursor.execute(del_diag, data_diag)
        mydb.commit()
        mydb.close()
        msg = "success"
        return msg
             
    except Exception as error:
        print(error)
        msg = "Error"
        return msg