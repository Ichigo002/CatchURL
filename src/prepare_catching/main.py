from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException

from ..utils.colorcmd import *
from ..utils.system_utils import *
from .usr_input_handling import *
from .fetchers.f_cda import *
from .fetchers.f_wbijam import *
from .fetchers.fetcher_template import *

from shutil import which

from pandas import *

def handle_driver_error(e, dr):
    setcol_error()
    if(type(e) == NoSuchWindowException):
        print("WebDriver window has been closed. Cannot keep going with program.")
    else:
        print("Critical Error occured: ", e)
    dr.quit()
    critical_exit()

def fuck_off_cookies(dr:webdriver.Chrome):
    try:
        dr.find_element(By.CLASS_NAME, "fc-cta-consent").click()
    except Exception as e:
        setcol_error()
        print("Cannot click cookies to stop annoying. It's not critical error ;)")
    setcol_success()
    print("(: Cookies clicked out automatically :)")

def make_new_df(filename, url):
    return DataFrame(
        {'filename':[filename],
        'status'  :[''],
        'url'     :[url]})

def add_new_url(cdf, filename, url):
    ndf = make_new_df(filename, url)
    return concat([cdf, ndf], ignore_index=True)


def main():
    init_colors()

    csv_name = fetch_any_usr_input("Type name of csv file where urls will be saved (example: 'testcsv')")
    

    pass_orig = fetch_usr_inputYN("Do you want use original video name to save")
    pattern_fname = "fetched-video-catchurl-%i"

    if not pass_orig:
        pattern_fname = fetch_any_usr_input("Type filename pattern (for instance: 'test-%') \n -> '%i' == index+1")

    df = DataFrame(columns=['filename', 'status', 'url'])
    
    setcol_decorative()
    print("\n  ---=*=---")

    url = "https://www.google.com"
    #url = "https://accelworld.wbijam.pl/odtwarzacz-_PLU_i3PZXb9BlAX6Qc_PLU_4_PLU_k8fEhdHYOqNOjP.html"

    dr = None
    if which('google-chrome') is not None: 
        setcol_info()
        print("Starting Chrome web driver...")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-features=NetworkService")
        chrome_options.add_argument("--disable-gpu")

        dr = webdriver.Chrome(chrome_options)
    
    elif which('firefox') is not None:
        setcol_info()
        print("Starting Firefox web driver...")

        dr = webdriver.Firefox()
    else:
        setcol_error()
        print("To proper work your OS has to have Firefox or Chrome.")
        critical_exit()
    

    setcol_info()
    print(f"Getting url: '{url}'")

    try:
        dr.get(url)
    except Exception as e:
        setcol_error()
        print("Error occured (Probably incorrect url address):\n", e)
        dr.quit()
        critical_exit()
    
    setcol_success()
    print("Website loaded successfully.")
    setcol_summary()
    print(" --==##==--")
    print(" Supported websites: ")
    print(" => www.cda.pl")
    print(" => wbijam.pl | only-players: cda.pl, dailymotion")
    print(" --==##==--")


    fuck_off_cookies(dr)

    index = 0
    fetcher = None

    ans = fetch_usr_inputYN("Are you ready to fetch first url?")
    while ans:
        vid = ""
        index += 1

        if dr.current_url.find("cda.pl") != -1:
            fetcher = Fetcher_cda(dr)
        elif dr.current_url.find("wbijam.pl") != -1:
            fetcher = Fetcher_wbijam(dr)
        else:
            setcol_error()
            print("This website isn't supported")
            ans = fetch_usr_inputYN("Do you want fetch next url?")
            continue

        try:
            break_v = False
            # HERE GET VIDeo url
            vid = fetcher.fetchVideo() 
            if fetcher.getErrno() == Errnos.ERROR:
                setcol_error()
                print("main.py:129 from instruction 'fetcher.fetchVideo() popped out naughty error.")
                handle_driver_error(fetcher.getErrmsg(), dr)
            elif fetcher.getErrno() == Errnos.EXCEPTION:
                setcol_error()
                print("Not dangerous error :) ", fetcher.getErrmsg())
                break_v = True

            if not break_v:
                fname = "error-filename"
                if pass_orig:
                    _fn = fetcher.fetchVideoTitle()
                    if _fn != None:
                        fname = _fn
                        if fetcher.getErrno() == Errnos.EXC_NO_PRIM_TITLE:
                            fname = f"{fname}-video-{index}"
                            setcol_info()
                            print(f"Video has got no specified name on this webpage. Used instead: '{fname}'")
                    else:
                        setcol_info()
                        print("Video has got no specified name on this webpage. Used default built-in name")
                        fname = pattern_fname.replace("%i", str(index))
                else:
                    fname = pattern_fname.replace("%i", str(index))
                df = add_new_url(df, fname, vid)
                setcol_success()
                print("URL has been fetched successfully")
        except Exception as e:
            setcol_error()
            print("main.py:128 instruction 'try' caught naughty error.")
            handle_driver_error(e, dr)

        ans = fetch_usr_inputYN("Do you want fetch next url?")


    fn = f"data/{csv_name}.csv"

    df.to_csv(fn, index=False)
    setcol_success()
    print(f"Successfully saved file: '{fn}'")

    sys_pause("BREAK: [END PROGRAM]\n Press Enter key to continue")

    setcol_info()
    print("Closing Web driver . . .")
    dr.quit()