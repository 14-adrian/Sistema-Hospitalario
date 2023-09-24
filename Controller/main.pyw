from __future__ import print_function
import eel
import pyautogui
from Models.login import login_user, login_session
 
actual_user = ''

eel.init('Views')
 
@eel.expose
def btn_login(user_name, password):
    msg = login_user(user_name, password)
    actual_user = user_name
    eel.login_return(str(msg))
 
@eel.expose
def get_user_online():
    get_user = actual_user
    print(get_user)
    eel.get_user(str(get_user))

@eel.expose
def new_window(target: str):
    eel.show(f"html/{target}")

     
eel.start(
    'templates/login.html',
    size=pyautogui.size(),
    jinja_templates='templates'
)