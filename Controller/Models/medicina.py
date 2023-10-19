import mysql.connector
from Models.conexion import myDB

def showallmedicina():
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM medicina")
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
    
def saveMedicina(id, desc):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        print(desc)
 
        if id != "" and desc != "":
            add_medici = """INSERT INTO `medicina` 
            (`idMedicina`, `Descripcion`)
             VALUES(%s, %s);"""
            data_medici = (id, desc)
            cursor.execute(add_medici, data_medici)
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
    
def showSelectedMedicina(id):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        print(id)
        sel_medici = """ SELECT * FROM `medicina` 
                            WHERE `idMedicina` = %s;"""
        data_medici = (id,)
        cursor.execute(sel_medici, data_medici)
        editarmedici = []
        for item in cursor.fetchone():
            editarmedici.append(item)
        return editarmedici
    except Exception as Error:
        print(Error)
        msg = "failure"
        return msg

def updateMedicina(id, desc):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        print(desc)
 
        if id != "" and desc != "" :
            upd_medici = """UPDATE `medicina` 
            SET `Descripcion` = %s 
            WHERE `medicina`.`idMedicina` = %s
            """
            data_medici = (desc, id)
            cursor.execute(upd_medici, data_medici)
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
    
def deleteMedicina(id):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        del_medici = """DELETE FROM medicina 
        WHERE `medicina`.`idMedicina` = %s
            """
        data_medici = (id,)
        cursor.execute(del_medici, data_medici)
        mydb.commit()
        mydb.close()
        msg = "success"
        return msg
             
    except Exception as error:
        print(error)
        msg = "Error"
        return msg