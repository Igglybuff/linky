from sys import exit


def error(silence=False, message='Unspecified failure!'):
    if silence is False:
        print('ERROR: ' + message)
        exit(1)


def info(silence=False, message='Success!'):
    if silence is False:
        print('INFO: ' + message)


def warning(silence=False, message='Generic warning!'):
    if silence is False:
        print('WARNING: ' + message)
