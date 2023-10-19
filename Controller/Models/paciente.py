import mysql.connector
from Models.conexion import myDB

def showallpacientes():
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM `paciente`")
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
    

def savePaciente(id, nombre, telefono, correo, fechaN, sexo, altura, peso):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        print(nombre)
 
        if id != "" and altura != "" and nombre != "" and telefono != ""and correo != "" and fechaN != "" and sexo != "" and peso != "":
            add_paciente = """INSERT INTO `paciente` 
            (`dui`, `nombrePaciente`, `telefonoPaciente`, `correoPaciente`, `fechaNacimiento`, `sexoPaciente`, `alturaPaciente`, `pesoPaciente`)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s);"""
            data_paciente = (id, nombre, telefono, correo, fechaN, sexo, altura, peso)
            cursor.execute(add_paciente, data_paciente)
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
    
def showSelectedPaciente(id):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        print(id)
        sel_pac = """ SELECT * FROM `paciente`
                            WHERE `dui` = %s;"""
        data_pac = (id,)
        cursor.execute(sel_pac, data_pac)
        editarpac = []
        for item in cursor.fetchone():
            editarpac.append(item)
        return editarpac
    except Exception as Error:
        print(Error)
        msg = "failure"
        return msg

def updatePaciente(id, nombre, telefono, correo, fechaN, sexo, altura, peso):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        print(nombre)
 
        if id != "" and altura != "" and nombre != "" and telefono != ""and correo != "" and fechaN != "" and sexo != "" and peso != "":
            upd_pac = """UPDATE `paciente` 
            SET `nombrePaciente` = %s,
              `telefonoPaciente` = %s, `correoPaciente` = %s,
                `fechaNacimiento` = %s, `sexoPaciente` = %s,
                  `alturaPaciente` = %s, `pesoPaciente` = %s 
                  WHERE `paciente`.`dui` = %s
            """
            data_pac = (nombre, telefono, correo, fechaN, sexo, altura, peso, id)
            cursor.execute(upd_pac, data_pac)
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
    
def deletePaciente(id):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        del_pac = """DELETE FROM paciente 
        WHERE `paciente`.`dui` = %s
            """
        data_pac = (id,)
        cursor.execute(del_pac, data_pac)
        mydb.commit()
        mydb.close()
        msg = "success"
        return msg
             
    except Exception as error:
        print(error)
        msg = "Error"
        return msg