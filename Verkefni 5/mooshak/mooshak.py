from flask import Flask, abort, request, render_template
from flask import redirect, url_for, send_from_directory
from flask import session, escape

import logging
import os
import sys
from os.path import join

from subsystem.auth import *
from models import *
from subsystem.filehandlers import file_pages
from subsystem.setupparser import *
from errorhandlers import new_errorhandlers

app = Flask(__name__)
new_errorhandlers(app)
auth_pages(app)
file_pages(app)

get_projects(app, 'projects')

@app.route('/')
def index():
    if check_logged(session):
        return check_logged(session)
    if 'username' in session:
        user = escape(session['username'])
        userprojects = []
        for key, entry in app.projects.items():
            if entry.is_member(user):
                userprojects.append(entry.render())
        return render_template('index.html', name=user, projects=userprojects)
    else:
        return redirect(url_for('logout'))

@app.route('/<int:id>')
def project(id):
    if check_logged(session):
        return check_logged(session)
    if not 'username' in session:
        return redirect(url_for('logout'))
    if not id in app.projects.keys():
        return redirect(url_for('index'))

    results = get_results(app, session, id)
    return render_template('project.html', name=escape(session['username']), project=app.projects[id].render(), results=results)

@app.route('/<int:id>/<int:entry>')
def details(id, entry):
    if check_logged(session):
        return check_logged(session)
    if not 'username' in session:
        return redirect(url_for('logout'))
    if not id in app.projects.keys():
        return redirect(url_for('index'))

    results = get_result(app, session, id, entry)
    if results:
        return render_template('details.html', name=escape(session['username']), project=app.projects[id].render(), results=results)
    return redirect(url_for('project', id))

if __name__ == '__main__':
    app.run(debug=True)
