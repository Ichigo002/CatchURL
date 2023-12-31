# this is downloader class.
# Created by Wiktor Bojanowksi. eee lu wo ma. Kaichou wa maid sama!
import urllib.request
import os
from ..utils import progress_bar, colorcmd as cc
from ..utils import system_utils as su

test_url = "https://vwaw501.cda.pl/RBgA-c8sHanoYBG0Jj42iA/1696200950/lq0751ce81093061a7090546f049e895bc.mp4"

class Downloader():
    
    __dwn_path__ = ""


    def __init__(self, default_path = "downloads"):
        self.__dwn_path__ = default_path
        print(f"[Default download path: \"{self.__dwn_path__}\"]")        


    def download_from_url(self, url, filename):
        if filename == ".mp4":
            cc.setcol_skip()
            print(" Warning: Row is empty. Skipping...")
            return -8

        if not os.path.exists(self.__dwn_path__):
            try:
                os.mkdir(self.__dwn_path__)        
            except FileNotFoundError:
                cc.setcol_error()
                print("Error. Cannot create directory. check if base folder 'downloads' exists.")
                return -6
            except Exception as e:
                cc.setcol_error()
                print("DIR ERROR: ", e)
                return -7
        
        cc.setcol_clear()
        print(f" Start downloading \"{filename}\"")
        fpath = self.__dwn_path__ + '/' + filename
        fpath = su.escape_path(fpath)
        try:
            urllib.request.urlretrieve(url, filename=fpath, reporthook=self.__report_hook__)
            print(end="\n")
        except urllib.error.HTTPError:
            cc.setcol_error()
            print("  HTTP ERROR: Forbidden, code 403. Cannot download")
            return -4
        except Exception as e:
            cc.setcol_error()
            print("  HTTP ERROR: ", e)
            return -5
        
        cc.setcol_success()
        print(f" File successfully downloaded")
        return 0

    def __report_hook__(self, block_num, block_size, total_size):
        progress_bar(block_num * block_size, total_size, 30)



    def shall_download(self, filename):
        return not os.path.exists(self.__dwn_path__ + '/' + filename)

    