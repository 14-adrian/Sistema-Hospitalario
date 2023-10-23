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

    
def saveUser(id, nombre, correo, dui, cargo, password, user):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        print(user)
 
        if id != "" and nombre != "" and correo != "" and dui != ""and cargo != "" and password != "" and user != "":
            add_diag = """INSERT INTO `usuarios` (`id`, `Nombre`, `Correo`, `DUI`, `Cargo`, `Contraseña`, `Usuario`) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            data_diag = (id, nombre, correo, dui, cargo, password, user)
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
    
def showSelectedUser(id):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        sel_diag = """ SELECT * FROM `usuarios`
                            WHERE `id` = %s;"""
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

def updateUser(id, nombre, correo, dui, cargo, password, user):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
 
        if id != "" and nombre != "" and correo != "" and dui != ""and cargo != "" and password != "" and user != "":
            upd_diag = """UPDATE `usuarios` 
            SET `Nombre` = %s, `Correo` = %s,
              `DUI` = %s, `Cargo` = %s,
                `Contraseña` = %s, `Usuario` = %s 
                WHERE `usuarios`.`id` = %s;
            """
            data_diag = (nombre, correo, dui, cargo, password, user, id)
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
    
def deleteUser(id):
    try:
        mydb = myDB()
        cursor = mydb.cursor()
        del_diag = """DELETE FROM usuarios 
        WHERE `usuarios`.`id` = %s
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