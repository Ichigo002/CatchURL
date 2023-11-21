from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException
from enum import Enum

class Errnos(Enum):
    SUCCESS = 0
    EXCEPTION = 1
    ERROR = -1

class BaseFetcher:
    def __init__(self, dr: webdriver.Chrome) -> None:
        self._dr = dr
        self._errno = Errnos.SUCCESS
        self._errmsg = ""

    """
    Return: URL video to download
    """
    def fetchVideo(self):
        v = "FetchVideo() ERROR. Piece of shittt. fuck this!!!"
        try:
            v = self._safeFetchVideo()
        except Exception as e:
            self._errno = Errnos.ERROR
            self._errmsg = e
        finally:
            return v

    def getErrno(self):
        return self._errno
    
    def getErrmsg(self):
        return self._errmsg
    
    """
    HERE PUT YOUR FETCH METHOD!!!!
    """
    def _safeFetchVideo(self):
        pass
    