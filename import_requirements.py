import requests
import platform
import os
import tarfile
import zipfile

def extract_file(path, to_directory='.'):
    if path.endswith('.zip'):
        opener, mode = zipfile.ZipFile, 'r'
    elif path.endswith('.tar.gz') or path.endswith('.tgz'):
        opener, mode = tarfile.open, 'r:gz'
    elif path.endswith('.tar.bz2') or path.endswith('.tbz'):
        opener, mode = tarfile.open, 'r:bz2'
    else: 
        raise ValueError

    cwd = os.getcwd()
    os.chdir(to_directory)

    try:
        file = opener(path, mode)
        try: file.extractall()
        finally: file.close()
    finally:
        os.chdir(cwd)

p = platform.system()
b = platform.architecture()[0]

# Processing-Py Command Line Tools

exists = os.path.isdir(os.path.dirname(os.path.realpath(__file__))+'/processing')

if not exists:
    if p == 'Linux' and b == '32bit':
        url = 'http://py.processing.org/processing.py-linux32.tgz'
        print('Downloading Processing.py Command Line Tools ... (~120MB)')
        r = requests.get(url, allow_redirects=True)
        open('processing.tgz', 'wb').write(r.content)
        print('Extracting file ...')
        extract_file('processing.tgz',os.path.dirname(os.path.realpath(__file__)))
    elif p == 'Linux' and b == '64bit':
        print('Downloading Processing.py Command Line Tools ... (~120MB)')
        url = 'http://py.processing.org/processing.py-linux64.tgz'
        r = requests.get(url, allow_redirects=True)
        open('processing.tgz', 'wb').write(r.content)
        print('Extracting file ...')
        extract_file('processing.tgz',os.path.dirname(os.path.realpath(__file__)))
    elif p == 'Windows' and b == '32bit':
        print('Downloading Processing.py Command Line Tools ... (~120MB)')
        url = 'http://py.processing.org/processing.py-windows32.zip'
        r = requests.get(url, allow_redirects=True)
        open('processing.zip', 'wb').write(r.content)
        print('Extracting file ...')
        extract_file('processing.zip',os.path.dirname(os.path.realpath(__file__)))
    elif p == 'Windows' and b == '64bit':
        print('Downloading Processing.py Command Line Tools ... (~120MB)')
        url = 'http://py.processing.org/processing.py-windows64.zip'
        r = requests.get(url, allow_redirects=True)
        open('processing.zip', 'wb').write(r.content)
        print('Extracting file ...')
        extract_file('processing.zip',os.path.dirname(os.path.realpath(__file__)))
    elif p == 'Darwin':
        print('Downloading Processing.py Command Line Tools ... (~120MB)')
        url = 'http://py.processing.org/processing.py-macosx.tgz'
        r = requests.get(url, allow_redirects=True)
        open('processing.tgz', 'wb').write(r.content)
        print('Extracting file ...')
        extract_file('processing.tgz')
    else:
        print('[ERROR] OS',p,b,'not supported')

# Java u802

