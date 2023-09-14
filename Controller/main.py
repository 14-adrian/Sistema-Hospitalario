from __future__ import print_function
import eel
from Models.login import login_user, login_session
 

eel.init('views')
 
@eel.expose
def btn_login(user_name, password):
    msg = login_user(user_name, password)
    eel.login_return(str(msg))
 
@eel.expose
def get_user_online():
    get_user = login_session()
    print(get_user)
    eel.get_user(str(get_user))
     
eel.start("index.html", size=(1366, 743))