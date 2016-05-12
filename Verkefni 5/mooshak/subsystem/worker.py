import threading
import time
import zipfile

import os
from os.path import join

def extract_zipfile(source, dest):
    try:
        with zipfile.ZipFile(source, 'r') as zipf:
                zipf.extractall(dest)
    except FileNotFoundError:
        with open(join(path, '__results__'), 'w') as cf:
            cf.write('Unable to extract zip file')
        return False
    except zipfile.BadZipFile:
        with open(join(path, '__results__'), 'w') as cf:
            cf.write('Unable to extract zip file')
        return False
    return True

def worker(path, project):
    if not extract_zipfile(join(path, str(project.id) + '.zip'), path):
        return

    listResults = []
    for case in project.testcases:
        with open(case[0],'r') as cppfile:
            with open(join(path, os.path.split(case[0])[1]), 'w') as output:
                output.write(cppfile.read())
        with open(case[1],'r') as expected:
            results = expected.read()

        listResults.append(['FAILURE', results])
    
    with open(join(path, '__results__'), 'w') as cf:
        cf.write('Success')
        for entry in listResults:
            cf.write('\n--\n{}\n--\n{}'.format(*entry))
    
def spawn_thread(path, project):
    t = threading.Thread(target=worker, args=(path,project))
    t.start()
