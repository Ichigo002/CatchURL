# this is downloader class.
# Created by Wiktor Bojanowksi. eee lu wo ma. Kaichou wa maid sama!
import urllib.request
import os

test_url = "https://vwaw501.cda.pl/RBgA-c8sHanoYBG0Jj42iA/1696200950/lq0751ce81093061a7090546f049e895bc.mp4"

class Downloader():
    
    __dwn_path__ = ""


    def __init__(self, default_path = "downloads"):
        self.__dwn_path__ = default_path
        print(f"Default download path: \"{self.__dwn_path__}\"")        


    def download_from_url(self, url, filename):
        if not os.path.exists(self.__dwn_path__):
            os.mkdir(self.__dwn_path__)        
        print(f"Start downloading \"{filename}\"")
        fpath = self.__dwn_path__ + '/' + filename + ".mp4"
        try:
            urllib.request.urlretrieve(url, filename=fpath)
        except:
            print("Error occurred")
            return -1
        
        print(f"File successfully downloaded")
        return 0

    def shall_download(self, filename):
        return not os.path.exists(self.__dwn_path__ + '/' + filename + ".mp4")

    