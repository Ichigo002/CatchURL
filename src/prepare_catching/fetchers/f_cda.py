from .fetcher_template import *

class Fetcher_cda(BaseFetcher):
    def _safeFetchVideo(self):
        print(self._dr.current_url)
        v = self._dr.find_elements(By.XPATH, '//video[@class="pb-video-player"]')
        src = v[0].get_attribute("src")
        return src