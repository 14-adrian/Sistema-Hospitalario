from __future__ import print_function
import eel
import pyautogui
from Models.login import login_user
from Models.medico import *
 
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
def get_registers():
    select_reg = showallmedicos()
    eel.action_out(select_reg)

     
eel.start(
    'templates/index.html',
    size=pyautogui.size(),
    jinja_templates='templates'
)

