from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_required
from login import login
from sensors import sensors
from actuators import actuators 

app = Flask(__name__)
app.secret_key = '123'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login.login_page'
app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensors, url_prefix='/')
app.register_blueprint(actuators, url_prefix='/')  

from flask_login import current_user
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('login.home'))
    return render_template('login.html')

@login_manager.user_loader
def load_user(user_id):
    from login import users, User
    if user_id in users:
        return User(user_id)
    return None
from app import login_manager
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)