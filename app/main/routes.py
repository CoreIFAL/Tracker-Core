from flask import render_template
        
from app.main import bp
from app.main.controller import list_active_sessions
from app.main.controller import get_data_by_username
from app.main.controller import how_many_access_by_labs
from app.main.controller import how_many_users_active
from app.models.user import User
from app.database import DB

@bp.route('/')
def index():
    users_front = list_active_sessions()
    length = how_many_users_active()
    return render_template('index.html', lista_users=users_front,active=length)

@bp.route('/grafico')
def chart():
    access_by_dates = how_many_access_by_labs()
    return render_template('grafico.html', datas=access_by_dates)

@bp.route('/user/<username>')
def get_user(username):
    user = get_data_by_username(username)
    return render_template('usuario.html', user=user)

