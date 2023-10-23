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
    
def saveMedico(id, esp, nombre, telefono, correo, fechaN, sexo):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        print(nombre)
 
        if id != "" and esp != "" and nombre != "" and telefono != ""and correo != "" and fechaN != "" and sexo != "":
            add_medico = """INSERT INTO `medico` 
            (`idMedico`, `especialidad`, `nombre`, `telefono`, `email`, `fechaNacimiento`, `sexo`) 
             VALUES(%s, %s, %s, %s, %s, %s, %s);"""
            data_medico = (id, esp, nombre, telefono, correo, fechaN, sexo)
            cursor.execute(add_medico, data_medico)
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
    
def showSelectedMedico(id):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        print(id)
        sel_medico = """ SELECT * FROM medico
                            WHERE `idMedico` = %s;"""
        data_medico = (id,)
        cursor.execute(sel_medico, data_medico)
        editarmedico = []
        for item in cursor.fetchone():
            editarmedico.append(item)
        return editarmedico
    except Exception as Error:
        print(Error)
        msg = "failure"
        return msg

def updateMedico(id, esp, nombre, telefono, correo, fechaN, sexo):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        print(nombre)
 
        if id != "" and esp != "" and nombre != "" and telefono != ""and correo != "" and fechaN != "" and sexo != "":
            upd_medico = """UPDATE `medico` 
            SET `especialidad` = %s, `nombre` = %s, `telefono` = %s, `email` = %s, `fechaNacimiento` = %s, `sexo` = %s 
            WHERE `medico`.`idMedico` = %s
            """
            data_medico = (esp, nombre, telefono, correo, fechaN, sexo, id)
            cursor.execute(upd_medico, data_medico)
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
    
def deleteMedico(id):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        del_medico = """DELETE FROM medico 
        WHERE `medico`.`idMedico` = %s
            """
        data_medico = (id,)
        cursor.execute(del_medico, data_medico)
        mydb.commit()
        mydb.close()
        msg = "success"
        return msg
             
    except Exception as error:
        print(error)
        msg = "Error"
        return msg