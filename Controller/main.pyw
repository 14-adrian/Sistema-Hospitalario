from __future__ import print_function
import eel
import pyautogui
from Models.login import login_user
from Models.medico import *
from Models.paciente import *
 
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

eel.start(
    'templates/index.html',
    size=pyautogui.size(),
    jinja_templates='templates'
)

