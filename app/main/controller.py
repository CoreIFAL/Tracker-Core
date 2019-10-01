from app.models.user import User

def list_active_sessions(list_users):
    active_sessions = []
    for i in list_users:
        if len(i['event']) % 2 != 0:
            user = User(i['name'], i['event'][-1]['operation'], i['event'][-1]['computername'], i['event'][-1]['date'], i['event'][-1]['time'])
            active_sessions.append(user)
    return active_sessions
    