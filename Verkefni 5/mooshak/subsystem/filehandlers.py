from subsystem.auth import check_logged
from flask import Flask, abort, session, request, escape, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import os
from os.path import join

def file_pages(app):
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    app.config['UPLOAD_FOLDER'] = 'user_files'

    @app.route('/upload', methods=['GET', 'POST'])
    def upload():
        
        if check_logged(session):
            return check_logged(session)
        if request.method != 'POST':
            return 'test'
            #(405)


        file = request.files['file']
        if file and 'username' in session and request.form['project']:
            path = join(join(app.config['UPLOAD_FOLDER'], escape(session['username'])), request.form['project'])
            try:
                os.makedirs(path)
            except FileExistsError:
                pass
            
            filename = secure_filename(file.filename)
            file.save(join(path, filename))
            return redirect(url_for('uploaded_file', filename=filename))
        else:
            return 'kappa'
            #abort(411)
    
    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        if check_logged(session):
            return check_logged(session)
        
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
