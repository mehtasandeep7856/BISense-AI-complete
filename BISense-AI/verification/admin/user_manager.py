from backend.app.models.user import User
def get_demo_user(username): return User(username=username,role='admin')
