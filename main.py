from __future__ import print_function
import eel
import pyautogui
from Models.login import login_user
from Models.medico import *
from Models.paciente import *
from Models.medicina import *
from Models.cita import *
from Models.diagnostico import *
from Models.usuarios import *
import json
import os
 
actual_user = 'empty'

eel.init('Views')
 
@eel.expose
def btn_login(user_name, password):
    global actual_user
    actual_user = user_name
    msg = login_user(user_name, password)
    eel.login_return(str(msg))
 
@eel.expose
def get_user_online():
    get_user = actual_user
    eel.get_user(str(get_user))

@eel.expose
def new_window(target: str):
    eel.show(f"html/{target}")

#------------CRUD MEDICOS--------------------

@eel.expose
def fetch_medicos():
    select_reg = showallmedicos()
    eel.action_out(select_reg)

@eel.expose 
def save_medico(id, esp, nombre, telefono, correo, fechaN, sexo):
    print(id, esp, nombre, telefono, correo, fechaN, sexo)
    msg = saveMedico(int(id), esp, nombre, telefono, correo, str(fechaN), sexo)
    print(msg)
    eel.save_return(str(msg))

@eel.expose
def get_medico(id):
    select_medico = showSelectedMedico(id)
    print(select_medico)
    eel.action_edit_m(select_medico)
     
@eel.expose 
def update_medico(id, esp, nombre, telefono, correo, fechaN, sexo):
    msg = updateMedico(id, esp, nombre, telefono, correo, fechaN, sexo)
    eel.update_return(str(msg))    
     
@eel.expose
def get_delete_medico(id):
    select_del_medico = deleteMedico(id)
    eel.delete_return(select_del_medico)

#------------CRUD PACIENTES--------------------
@eel.expose
def fetch_pacientes():
    select_reg = showallpacientes()
    eel.action_out(select_reg)

@eel.expose 
def save_paciente(id, nombre, telefono, correo, fechaN, sexo, altura, peso):
    print(id, nombre, telefono, correo, fechaN, sexo, altura, peso)
    msg = savePaciente(int(id), nombre, telefono, correo, fechaN, sexo, altura, peso)
    print(msg)
    eel.save_return(str(msg))

@eel.expose
def get_paciente(id):
    select_pac = showSelectedPaciente(id)
    print(select_pac)
    eel.action_edit_m(select_pac)
     
@eel.expose 
def update_paciente(id, nombre, telefono, correo, fechaN, sexo, altura, peso):
    msg = updatePaciente(id, nombre, telefono, correo, fechaN, sexo, altura, peso)
    eel.update_return(str(msg))    
     
@eel.expose
def get_delete_paciente(id):
    select_del_pac = deletePaciente(id)
    eel.delete_return(select_del_pac)

#--------------CRUD MEDICINA----------------------
@eel.expose
def fetch_medicina():
    select_reg = showallmedicina()
    eel.action_out(select_reg)

@eel.expose 
def save_medicina(id, desc):
    print(id, desc)
    msg = saveMedicina(int(id), desc)
    print(msg)
    eel.save_return(str(msg))

@eel.expose
def get_medicina(id):
    select_medici = showSelectedMedicina(id)
    print(select_medici)
    eel.action_edit_m(select_medici)
     
@eel.expose 
def update_medicina(id, desc):
    msg = updateMedicina(id, desc)
    eel.update_return(str(msg))    
     
@eel.expose
def get_delete_medicina(id):
    select_del_medici = deleteMedicina(id)
    eel.delete_return(select_del_medici)

#-------------CRUD CITAS-----------------------
@eel.expose
def fetch_citas():
    select_reg = showallcitas()
    eel.action_out(select_reg)

@eel.expose
def get_NMedico():
    select_reg = showNombreM()
    eel.action_NM(select_reg)

@eel.expose
def get_NPaciente():
    select_reg = showNombreP()
    eel.action_NP(select_reg)

@eel.expose 
def save_cita(id, nombreM, nombreP, tipo, fecha, estado):
    print(id, nombreM, nombreP, tipo, fecha, estado)
    msg = saveCita(int(id), nombreM, nombreP, tipo, fecha, estado)
    print(msg)
    eel.save_return(str(msg))

@eel.expose
def get_cita(id):
    select_cita = showSelectedCita(id)
    print(select_cita)
    eel.action_edit_m(select_cita)
     
@eel.expose 
def update_cita(id, nombreM, nombreP, tipo, fecha, estado):
    msg = updateCita(id, nombreM, nombreP, tipo, fecha, estado)
    eel.update_return(str(msg))    
     
@eel.expose
def get_delete_cita(id):
    select_del_cita = deleteCita(id)
    eel.delete_return(select_del_cita)

#-------------CRUD DIAGNOSTICOS------------------
@eel.expose
def fetch_diag():
    select_reg = showalldiag()
    eel.action_out(select_reg)

@eel.expose
def get_DMedico():
    select_reg = showNombreMD()
    eel.action_NM(select_reg)

@eel.expose
def get_DPaciente():
    select_reg = showNombrePD()
    eel.action_NP(select_reg)

@eel.expose
def get_DMedicina():
    select_reg = showLstMed()
    eel.action_MD(select_reg)

@eel.expose 
def save_diag(id, paciente, medico, idc, desc, medicina):
    print(id, paciente, medico, idc, desc, medicina)
    msg = saveDiag(int(id), paciente, medico, idc, desc, medicina)
    print(msg)
    eel.save_return(str(msg))

@eel.expose
def get_diag(id):
    select_diag = showSelectedDiag(id)
    print(select_diag)
    eel.action_edit_m(select_diag)
     
@eel.expose 
def update_diag(id, paciente, medico, idc, desc, medicina):
    msg = updateDiag(id, paciente, medico, idc, desc, medicina)
    eel.update_return(str(msg))    
     
@eel.expose
def get_delete_diag(id):
    select_del_diag = deleteDiag(id)
    eel.delete_return(select_del_diag)


#----------------CRUD USUARIOS---------------------
@eel.expose
def fetch_users():
    select_reg = showallusers()
    eel.action_out(select_reg)

@eel.expose 
def save_users(id, nombre, correo, dui, cargo, password, user):
    print(id, nombre, correo, dui, cargo, password, user)
    msg = saveUser(int(id),nombre, correo, dui, cargo, password, user)
    print(msg)
    eel.save_return(str(msg))

@eel.expose
def get_user(id):
    select_medico = showSelectedUser(id)
    print(select_medico)
    eel.action_edit_m(select_medico)
     
@eel.expose 
def update_user(id, nombre, correo, dui, cargo, password, user):
    msg = updateUser(id, nombre, correo, dui, cargo, password, user)
    eel.update_return(str(msg))    
     
@eel.expose
def get_delete_user(id):
    select_del_medico = deleteUser(id)
    eel.delete_return(select_del_medico)
    

@eel.expose
def config():
    eel.start(
        'templates/config.html',
        size="400x300",
        port = "8080",
        jinja_templates='templates'
    )

with open('Models/conexion.json', 'r') as f:
        data = json.load(f)
data_val = list(data.values())

@eel.expose
def update_conf(host, user, passw, db):
    filename = 'Models/conexion.json'
    with open(filename, 'r') as f:
        dato = json.load(f)
        dato['host'] = host
        dato['user'] = user
        dato['password'] = passw
        dato['database'] = db

    os.remove(filename)
    with open(filename, 'w') as f:
        json.dump(dato, f, indent=4)

    
       

@eel.expose
def getDataJson():
    
    return data_val

eel.start(
    'templates/login.html',
    size=pyautogui.size(),
    jinja_templates='templates'
)

