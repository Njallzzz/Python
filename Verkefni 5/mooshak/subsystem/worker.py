import threading
import time
import zipfile
import subprocess
import signal
import os
import re

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

def compile_program(path, file):
    source = join(path, file)
    dest = join(path, os.path.splitext(file)[0])
    # Fix sometime
    others = [ join(path, 'myclass.cpp') ]
    #
    compiler_params = ['g++', '-o', dest, source]
    compiler_params.extend(others)
    try:
        response = subprocess.run(compiler_params, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=15, env=os.environ.copy())
    except subprocess.TimeoutExpired:
        return 'Compiler timeout: occured after 15s'
    if response.returncode:
        return 'Compiler error: {}'.format(response.stderr.decode('UTF-8'))
    return False

def run_test(program):
    try:
        response = subprocess.run(program, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=15)
    except subprocess.TimeoutExpired:
        return TimeoutError('Timeout occured after 15 seconds')
    return response.stdout.decode('UTF-8')

def worker(path, project):
    if not extract_zipfile(join(path, str(project.id) + '.zip'), path):
        return
    listResults = []
    testresults = None
    for case in project.testcases:
        with open(case[0],'r') as cppfile:
            with open(join(path, os.path.split(case[0])[1]), 'w') as output:
                output.write(cppfile.read())
        with open(case[1],'r') as expected:
            results = expected.read()

        compileoutput = compile_program(path, os.path.split(case[0])[1])
        if compileoutput:
            if not testresults:
                testresults = re.search(r'(Compiler [^:]*)', compileoutput).group(1)
            listResults.append([compileoutput, results])
        else:
            runoutput = run_test(join(path, os.path.splitext(os.path.split(case[0])[1])[0] + '.exe')).replace('\r', '')
            if runoutput == TimeoutError:
                if not testresults:
                    testresults = 'Runtime Timeout'
                listResults.append([runoutput.args[0], results])
            else:
                listResults.append([runoutput, results])

    if not testresults:
        if any(list(map(lambda x: x[0] != x[1], listResults))):
            testresults = 'Incorrect output'
        else:
            testresults = 'Accepted'
    with open(join(path, '__results__'), 'w') as cf:
        cf.write(testresults)
        for entry in listResults:
            cf.write('\n--\n{}\n--\n{}'.format(*entry))
    
def spawn_thread(path, project):
    t = threading.Thread(target=worker, args=(path,project))
    t.start()
