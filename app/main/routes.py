from flask import render_template
        
from app.main import bp
from app.main.controller import list_active_sessions
from app.models.user import User
from app.database import DB

@bp.route('/')
def index():
    lista_users = DB.find_all('users')
    users_front = list_active_sessions(lista_users)
    return render_template('index.html', lista_users=users_front,active=len(users_front))
