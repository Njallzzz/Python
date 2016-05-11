from flask import session, request, redirect, url_for, render_template
from passlib.apps import custom_app_context as pwd_context
import os

def check_logged(session):
    if not 'username' in session:
        return redirect(url_for('login'))
    return False

class Auth_Master():
    def __init__(self):        
        self.users = {'admin': pwd_context.encrypt(''),
                      'kappa123': pwd_context.encrypt('123'),
                      'nokappa': pwd_context.encrypt('123') }

    def valid_login(self, username, password):
        if username in self.users.keys():
            return pwd_context.verify(password, self.users[username])
        return False

def auth_pages(app):
    app.secret_key = os.urandom(24)
    app.auth = Auth_Master()

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            if app.auth.valid_login(request.form['username'], request.form['password']):
                session['username'] = request.form['username']
                session['password'] = request.form['password']
                return redirect(url_for('index'))
        return render_template('login.html')

    @app.route('/logout')
    def logout():
        # remove the username from the session if it's there
        session.pop('username', None)
        return redirect(url_for('login'))
