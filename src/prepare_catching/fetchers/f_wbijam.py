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
            # future cases . . . 

    def _checkPlayer(self):
        print("chekcPayere")
        src = self._dr.find_elements(By.TAG_NAME, "iframe")[0].get_attribute("src")
        return src.split("/", 3)[2]