from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException
from shutil import which

from .colorcmd import *
from .system_utils import critical_exit

def getWebDriver():
    if which('google-chrome') is not None: 
        setcol_info()
        print("Starting Chrome web driver...")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-features=NetworkService")
        chrome_options.add_argument("--disable-gpu")

        return webdriver.Chrome(chrome_options)
    
    elif which('firefox') is not None:
        setcol_info()
        print("Starting Firefox web driver...")

        return webdriver.Firefox()
        
    setcol_error()
    print("To proper work your OS has to have Firefox or Chrome.")
    critical_exit()
    
default_class_cookie = [
    "fc-cta-consent", # cda.pl
    "W0wltc", # google.com
    "e1sXLPUy", # wbijam.pl
    ]

def fuckOffCookies(dr : webdriver.Chrome, additional_cookie_class = ""):
    cp_dcc = default_class_cookie.copy()
    
    if additional_cookie_class != "":
        cp_dcc.append(additional_cookie_class)

    done = True
    for elem in cp_dcc:
        done = True
        try:
            dr.find_element(By.CLASS_NAME, elem).click()
        except Exception as e:
            done = False
        if done:
            setcol_success()
            print("(: Cookies clicked out automatically :)")
            return
