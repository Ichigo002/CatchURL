from .fetcher_template import *

class Fetcher_cda(BaseFetcher):
    def _safeFetchVideo(self):
            return self._dr.find_elements(By.CLASS_NAME, "pb-video-player")[0].get_attribute("src") 