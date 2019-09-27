from app import app
from flask import render_template
from jinja2 import Environment, FileSystemLoader

#env = Environment(loader=FileSystemLoader('frontdesk/templates'))
#template = env.get_template('index.html')

@app.route('/')
@app.route('/index')
def index():
    user1={'username': 'Miguel'}
    user2={'username': 'Mauro'}
    user3={'username': 'Alexandro'}
    users = [user1,user2,user3]
    return render_template("index.html", users = users, user1 = user1, user2 = user2, user3 = user3)
