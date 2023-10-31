from colorama import Fore, Style, init

def init_colors():
    init()

def setcol_error():
    print(Fore.RED, end="")

def setcol_success():
    print(Fore.GREEN, end="")

def setcol_summary():
    print(Fore.LIGHTYELLOW_EX, end="")

def setcol_info():
    print(Fore.WHITE, end="")

def setcol_skip():
    print(Fore.CYAN, end="")

def setcol_question():
    print(Fore.LIGHTMAGENTA_EX, end="")

def setcol_user_input():
    print(Fore.LIGHTYELLOW_EX, end="")

def setcol_clear():
    print(Style.RESET_ALL, end="")

def setcol_decorative():
    print(Fore.CYAN, end="")