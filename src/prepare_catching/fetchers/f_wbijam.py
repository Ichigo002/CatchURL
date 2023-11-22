from .fetcher_template import *
from .f_cda import Fetcher_cda

class Fetcher_wbijam(BaseFetcher):
    def _safeFetchVideo(self):
        src = self.getIFrameSrc()
        match self._checkPlayer(src[0]):
            case "ebd.cda.pl":
                self._dr.switch_to.frame(src[1])
                video = self._dr.find_elements(By.CLASS_NAME, "pb-video-player")
                _src = video[0].get_attribute("src")
                
                return _src
            case "www.dailymotion.com":
                return src[0]
            case _:
                return None
            # future cases . . . 

    def _getVideoTitle(self):
        self._errno = Errnos.EXC_NO_PRIM_TITLE
        self._errmsg = "EXC_NO_PRIM_TITLE means video title returned most accurate title"
        dotted_title = self._dr.current_url.split("/")[2]
        title = dotted_title.split(".")[0]
        return title

    def _checkPlayer(self, src):
        try:
            t = src.split("/", 3)
            return t[2]
        except Exception as e:
            self._errno = Errnos.EXCEPTION
            self._errmsg = f"Something went wrong. Maybe webpage hasn't loaded yet."
            if src == '':
                self._errmsg += " Warning at _checkPlayer() at f_wbijam.py variable src is empty!!"
            return ""

    def getIFrameSrc(self):
        list = self._dr.find_elements(By.TAG_NAME, "iframe")
        src = None
        for el in list:
            src = el.get_attribute("src") 
            if src != '':
                return [src, el]
 
            