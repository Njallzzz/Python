from models import Project
from flask import escape, session

import os
from os.path import join

def setup_parser(project, file):
    with open(file, encoding='UTF-8') as cf:
        data = cf.read().split('--')

    name = data[0].strip('\n')
    if data[1].startswith('\n'):
        desc = data[1][1:].replace('\n', '<br>')
    else:
        desc = data[1].replace('\n', '<br>')
    url = data[2].strip('\n')
    desc = desc.format(URL='<a href="{}">{}</a>'.format(url, os.path.split(url)[1]))
    
    userlist = data[3].lower().strip('\n').split(' ')
    
    path = os.path.split(file)[0]
    testcases = []
    for entry in [ x for x in data[4].splitlines() if x ]:
        testcases.append([ join(path, x) for x in entry.split(' ') ])
    
    result = Project(project, name, desc)
    result.add_members(userlist)
    result.add_testcases(testcases)
    return result

def get_projects(app, path):
    app.projects = {}
    for path, subdirs, files in os.walk(path):
        for file in files:
            if 'setup' == file:
                projectid = int(os.path.split(path)[1])
                app.projects[projectid] = setup_parser(projectid, join(path, file))

def get_results(app, session, project):
    results = []
    d = join(join(app.config['UPLOAD_FOLDER'], escape(session['username'])), str(project))
    for path, subdirs, files in os.walk(d):
        for file in files:
            if '__results__' == file:
                with open(join(path, file)) as cf:
                    results.append([ os.path.split(path)[-1], cf.read().splitlines()[0]])
    return sorted(results, key=lambda x: x[0], reverse=True)

def get_result(app, session, project, entry):
    results = []
    d = join(join(app.config['UPLOAD_FOLDER'], escape(session['username'])), str(project))
    for path, subdirs, files in os.walk(d):
        for file in files:
            if '__results__' == file:
                with open(join(path, file)) as cf:
                    results.append([ os.path.split(path)[-1], cf.read().splitlines()[0]])
    return sorted(results, key=lambda x: x[0], reverse=True)
