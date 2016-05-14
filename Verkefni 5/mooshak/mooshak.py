from flask import Flask, abort, request, render_template
from flask import redirect, url_for, send_from_directory
from flask import session, escape

import logging
import logging.handlers
import os
import sys
from os.path import join

from subsystem.auth import *
from models import *
from subsystem.filehandlers import file_pages
from subsystem.setupparser import *
from errorhandlers import new_errorhandlers

app = Flask(__name__)
accesslogger = logging.getLogger('werkzeug')
rotaccesshandler = logging.handlers.RotatingFileHandler('access.log', maxBytes=1024*1024*25, backupCount=10)
rotaccesshandler.setLevel(logging.DEBUG)
accesslogger.addHandler(rotaccesshandler)

errorlogger = logging.getLogger('werkzeug')
roterrorhandler = logging.handlers.RotatingFileHandler('error.log', maxBytes=1024*1024*25, backupCount=10)
roterrorhandler.setLevel(logging.WARNING)
errorlogger.addHandler(roterrorhandler)
app.logger.addHandler(roterrorhandler)

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
        if app.auth.is_mod(user):
            return render_template('index.html', name=user, projects=userprojects, mod=True)
        else:
            return render_template('index.html', name=user, projects=userprojects)
    else:
        return redirect(url_for('logout'))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if check_logged(session):
        return check_logged(session)
    if 'username' in session:
        user = escape(session['username'])
        if not app.auth.is_mod(user):
            abort(404)
        if request.method == 'POST':
            entries = list(request.form.keys())
            if 'button' in entries:
                if request.form['button'] == 'projects':
                    get_projects(app, 'projects')
                elif request.form['button'] == 'users':
                    app.auth.retrieve_database()
            elif 'username' in entries and 'password' in entries:
                app.auth.create_user(request.form['username'], request.form['password'], '')
        return render_template('admin.html', name=user, users=app.auth.list_users())
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
    return render_template('project.html', name=escape(session['username']), project=app.projects[id].render(),
                           results=results, maxfilesize=app.config['MAX_CONTENT_LENGTH']/(1024*1024), allowed_extensions=app.allowed_extensions)

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
    app.run()
