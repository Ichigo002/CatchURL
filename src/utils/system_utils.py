from .colorcmd import setcol_clear
import os
import platform

def critical_exit():
    setcol_clear()
    print('\nCritical exit.')
    sys_pause()
    os._exit(-1)

def escape_path(path : str):
    if if_linux():
        return path.replace("\\", "/")
    else:
        return path.replace("/", "\\")

def sys_pause(text_info="Press Enter key to continue . . ."):
    setcol_clear()
    print()
    if if_linux():
        os.system(f'read -r -p "{text_info}" key')
    else:
        print(text_info)
        os.system("pause")
    print()

def if_linux():
    return platform.system() == "Linux"