from .colorcmd import setcol_clear
import os

def critical_exit():
    setcol_clear()
    print('\nCritical exit.')
    sys_pause()
    os._exit(-1)

def sys_pause(text_info="Press any key to continue . . ."):
     setcol_clear()
     os.system(f'read -n1 -r -p "{text_info}" key')