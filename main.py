from PyInquirer import prompt, print_json
from sys import argv
from os.path import isfile, join
from os import listdir, system
from pathlib import Path

SCRIPT_FOLDER = str(Path.home()) + '/.redo/scripts/'


def get_scripts():
    return [s for s in listdir(SCRIPT_FOLDER) if isfile(join(SCRIPT_FOLDER, s))]


def listScripts():
    return {
        'type': 'list',
        'name': 'script',
        'message': 'Running',
        'choices': get_scripts()
    }


if __name__ == "__main__":
    if len(argv) == 1:
        script = prompt(listScripts())['script']
        system(SCRIPT_FOLDER + script)