from subsystem.auth import check_logged
from subsystem.worker import spawn_thread
from flask import Flask, abort, session, request, escape, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import os
from os.path import join

def file_pages(app):
    app.config['MAX_CONTENT_LENGTH'] = 256 * 1024 * 1024
    app.config['UPLOAD_FOLDER'] = 'user_files'

    @app.route('/upload', methods=['GET', 'POST'])
    def upload():
        
        if check_logged(session):
            return check_logged(session)
        if request.method != 'POST':
            abort(405)


        file = request.files['file']
        if file and 'username' in session and request.form['project']:
            if (not request.form['project'].isdigit()) or (not int(request.form['project']) in app.projects.keys()):
                abort(411)
                
            path = join(join(app.config['UPLOAD_FOLDER'], escape(session['username'])), request.form['project'])
            try:
                os.makedirs(path)
            except FileExistsError:
                pass
            _, subdirs, _ = next(os.walk(path))

            lastEntry = 0
            for subdir in subdirs:
                if subdir.isdigit() and int(subdir) > lastEntry:
                    lastEntry = int(subdir)
            lastEntry = lastEntry + 1
            path = join(path, str(lastEntry))
            try:
                os.makedirs(path)
            except FileExistsError:
                pass
            
            file.save(join(path, request.form['project'] + '.zip'))
            with open(join(path, '__results__'), 'w') as cf:
                cf.write('In Progress')
            spawn_thread(path, app.projects[int(request.form['project'])])
            return redirect(url_for('project', id=request.form['project']))
        else:
            abort(411)
