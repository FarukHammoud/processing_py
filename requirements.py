import requests
import platform
import os
import zipfile
from clint.textui import progress,colored, puts

def extract_file(path, to_directory='.'):
    if path.endswith('.zip'):
        opener, mode = zipfile.ZipFile, 'r'
    else: 
        raise ValueError

    cwd = os.getcwd()
    os.chdir(to_directory)

    try:
        file = opener(path, mode)
        try: file.extractall()
        finally: file.close()
    finally:
        os.remove(path)
        os.chdir(cwd)
        
def download_processing():

    package_folder = os.path.dirname(os.path.realpath(__file__))
    p = platform.system()
    b = platform.architecture()[0]

    if p == 'Linux' and b == '32bit':
        url = 'https://github.com/FarukHammoud/processing_py/raw/master/repo/processing_linux32.zip'
    elif p == 'Linux' and b == '64bit':
        url = 'https://github.com/FarukHammoud/processing_py/raw/master/repo/processing_linux64.zip'
    elif p == 'Windows' and b == '32bit':
        url = 'https://github.com/FarukHammoud/processing_py/raw/master/repo/processing_win32.zip'
    elif p == 'Windows' and b == '64bit':
        url = 'https://github.com/FarukHammoud/processing_py/raw/master/repo/processing_win64.zip'
    elif p == 'Darwin':
        url = 'https://github.com/FarukHammoud/processing_py/raw/master/repo/processing_macos.zip'
    else:
        print('[ERROR] OS',p,b,'not supported')
        return 0

    print('Downloading Processing.py & Java Runtime Environment 8u202 ... (~120MB)')

    r = requests.get(url, stream=True)
    with open(package_folder+'/processing.zip', 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
            if chunk:
                f.write(chunk)
                f.flush()

    print('Extracting file ...')
    extract_file('processing.zip',os.path.dirname(os.path.realpath(__file__)))

    if p == 'Darwin' or p == 'Linux':
        os.chmod(package_folder+"/processing/jre/bin/java", 0o775)
    elif p == 'Windows':
        os.chmod(package_folder+"/processing/jre/bin/java.exe", 0o775)
    
def check_requirements():

    package_folder = os.path.dirname(os.path.realpath(__file__))

    # Processing-Py Command Line Tools
    processing_folder_downloaded = os.path.isdir(package_folder+'/processing')

    if not processing_folder_downloaded:
        download_processing()
        