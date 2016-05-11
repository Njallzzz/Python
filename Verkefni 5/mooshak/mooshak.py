from flask import Flask, abort, request, render_template
from flask import redirect, url_for, send_from_directory
from flask import session, escape


import os
from os.path import join

from subsystem.auth import *
from subsystem.filehandlers import file_pages
from errorhandlers import new_errorhandlers

app = Flask(__name__)
new_errorhandlers(app)
auth_pages(app)
file_pages(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if check_logged(session):
        return check_logged(session)
    if 'username' in session:
        return render_template('index.html', name=escape(session['username']))
    else:
        return redirect(url_for('logout'))

if __name__ == '__main__':
    app.run(debug=True)
