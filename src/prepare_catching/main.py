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

from pandas import *

def handle_driver_error(e, dr):
    setcol_error()
    if(type(e) == NoSuchWindowException):
        print("Chrome window has been closed. Cannot keep going with program.")
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
    pattern_fname = ""

    if not pass_orig:
        pattern_fname = fetch_any_usr_input("Type filename pattern (for instance: 'test-%') \n -> '%i' == index+1")

    df = DataFrame(columns=['filename', 'status', 'url'])
    
    setcol_decorative()
    print("\n  ---=*=---")

    url = "https://www.cda.pl"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-features=NetworkService")
    chrome_options.add_argument("--disable-gpu")

    dr = webdriver.Chrome(chrome_options)

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
    print("Webpage loaded successfully.")

    fuck_off_cookies(dr)

    index = 0

    ans = fetch_usr_inputYN("Are you ready to fetch first url?")
    while ans:
        vid = ""
        index += 1

        fetcher = Fetcher_cda(dr)

        try:
            # HERE GET VIDeo url
            vid = fetcher.fetchVideo() 
            if fetcher.getErrno() != Errnos.SUCCESS:
                handle_driver_error(fetcher.getErrmsg(), dr)
                
            fname = "error-filename"
            if pass_orig:
                span = dr.find_elements(By.CLASS_NAME, "title-name")[0]
                fname = span.find_elements(By.TAG_NAME, "span")[0].find_element(By.TAG_NAME, "h1").text
            else:
                fname = pattern_fname.replace("%i", str(index))
            df = add_new_url(df, fname, vid)
        except Exception as e:
            handle_driver_error(e, dr)
        finally:
            setcol_success()
            print("URL has been fetched successfully")

        ans = fetch_usr_inputYN("Do you want fetch next url?")


    fn = f"data/{csv_name}.csv"

    df.to_csv(fn, index=False)
    setcol_success()
    print(f"Successfully saved file: '{fn}'")

    sys_pause("BREAK: [END PROGRAM]")

    setcol_info()
    print("Closing chrome . . .")
    dr.quit()