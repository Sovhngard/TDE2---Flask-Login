from flask_login import UserMixin, login_user, logout_user, login_required
from flask import Blueprint, render_template, request, redirect, url_for

login = Blueprint("login", __name__ , template_folder="templates")

users = {
    "user1":"1234",
    "user2":"12345"
}

class User(UserMixin):
    def __init__(self, username):
        self.id = username

@login.route('/validated_user', methods=['POST'])
def validated_user():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']

        if user in users and users[user] == password:
            user_obj = User(user)
            login_user(user_obj)
            return render_template('home.html')

        return render_template('login.html', error="Usuário ou senha inválidos!")

    return render_template('login.html')

@login.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.login_page'))

@login.route('/login')
def login_page():
    return render_template('login.html')

@login.route('/list_users')
@login_required 
def list_users():
    global users
    return render_template("users.html", devices=users)

@login.route('/register_user')
def register_user():
    return render_template("register_user.html")

@login.route('/add_user', methods=['GET', 'POST'])
def add_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
    else:
        user = request.args.get('user', None)
        password = request.args.get('password', None)
    users[user] = password
    return render_template("users.html", devices=users)
@login.route('/home')
@login_required
def home():
    return render_template('home.html')

@login.route('/remove_user')
@login_required 
def remove_user():
    return render_template("remove_user.html", devices=users)

@login.route('/del_user', methods=['GET', 'POST'])
@login_required 
def del_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
    else:
        user = request.args.get('user', None)
    users.pop(user, None)
    return render_template("users.html", devices=users)
