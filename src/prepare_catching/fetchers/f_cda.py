from .fetcher_template import *

class Fetcher_cda(BaseFetcher):
    def _safeFetchVideo(self):
        print(self._dr.current_url)
        v = self._dr.find_elements(By.XPATH, '//video[@class="pb-video-player"]')
        src = v[0].get_attribute("src")
        return src

    def _getVideoTitle(self):
        span = self._dr.find_elements(By.CLASS_NAME, "title-name")[0]
        fname = span.find_elements(By.TAG_NAME, "span")[0].find_element(By.TAG_NAME, "h1").text
        return fname
