import subprocess
from properties import *

properties = [NAME, FPS, QUALITY, DIRECTORY, EXPORT]
properties = ','.join(map(str, properties))


def run_bash_function(library_path, function_name, params):
    p = subprocess.Popen(
        [
            'bash', '-c',
            '. %s; %s %s' % (library_path, function_name, params)
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return p.stdout.read().strip()


def export():
    run_bash_function('scripts', 'export', properties)


def listFiles():
    run_bash_function('scripts', 'listFiles', properties)


def render():
    run_bash_function('scripts', 'render', properties)


def rename():
    run_bash_function('scripts', 'rename', properties)