
import mysql.connector
from Models.conexion import myDB
 
def login_user(user_name, password):
    print(user_name)
    print(password)
    
    try:
        mydb = myDB()
        #connect = sqlite3.connect("views/database/storage.db")
        #cursor = connect.cursor()
        cursor = mydb.cursor()
        cursor.execute(
            "SELECT Password FROM users WHERE User=%s",(user_name,))
        get_password = cursor.fetchone()
        if password == get_password[0]:
            msg = "success"
            
            mydb.close()
            return msg
        else:
            msg = "failed"
            mydb.close()
            return msg
 
    except Exception as Error:
        print(Error)
        msg = "failed"
        return msg
 
 
def login_session():
    try:
        mydb = myDB()
        #connect = sqlite3.connect("views/database/storage.db")
        #cursor = connect.cursor()
        cursor = mydb.cursor()
        cursor.execute("SELECT User FROM user_session WHERE id =%s", (1,))
        get_user_online = cursor.fetchone()
        user_online = []
        for name in get_user_online:
            user_online.append(name)
        mydb.close()
        return user_online[0]
    except Exception as error:
        user_online = "error"
        print(error)
        return user_online
    