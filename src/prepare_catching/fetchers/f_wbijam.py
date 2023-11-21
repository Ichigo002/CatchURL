from .fetcher_template import *
from .f_cda import Fetcher_cda

class Fetcher_wbijam(BaseFetcher):
    def _safeFetchVideo(self):
        match self._checkPlayer():
            case "ebd.cda.pl":
                f = Fetcher_cda(self._dr)
                return f.fetchVideo()
            case "www.dailymotion.com":
                return self._dr.find_elements(By.TAG_NAME, "iframe")[0].get_attribute("src")
            case _:
                return None
            # future cases . . . 

    def _checkPlayer(self):
        src = self._dr.find_elements(By.TAG_NAME, "iframe")[0].get_attribute("src")
        try:
            t = src.split("/", 2)
            return t[2]
        except Exception as e:
            self._errno = Errnos.EXCEPTION
            self._errmsg = f"Something went wrong. Maybe webpage hasn't loaded yet."
            return ""
            