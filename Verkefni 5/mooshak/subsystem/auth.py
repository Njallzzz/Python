from flask import session, request, redirect, url_for, render_template
from passlib.apps import custom_app_context as pwd_context
import os
import sqlite3

def check_logged(session):
    if not 'username' in session:
        return redirect(url_for('login'))
    return False

class Auth_Master():
    def __init__(self):
        self.users = {}
        
        self.retrieve_database()
        
    def create_user(self, username, password, mod):
        if not username in self.users.keys():
            self.conn = sqlite3.connect('users.db')
            self.c = self.conn.cursor()
            self.users[username] = pwd_context.encrypt(password)
            query = 'INSERT INTO users VALUES (\'{user}\', \'{password}\', \'{mod}\')'.format(user=username, password=self.users[username], mod=mod)
            self.c.execute(query)
            self.conn.commit()
            self.conn.close()

    def __del__(self):
        self.conn.close()

    def list_users(self):
        return self.users.keys()

    def retrieve_database(self):
        self.conn = sqlite3.connect('users.db')
        self.c = self.conn.cursor()
        for row in self.c.execute('SELECT * FROM users'):
            self.users[row[0]] = row[1:]
        self.conn.close()

    def is_mod(self, username):
        return self.users[username][1] == 'a'

    def valid_login(self, username, password):
        if username in self.users.keys():
            return pwd_context.verify(password, self.users[username][0])
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
