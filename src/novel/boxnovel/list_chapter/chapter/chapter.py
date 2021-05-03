from bs4 import BeautifulSoup
import requests_async as requests

class Chapter:
    def __init__(self, url: str):
        self._url: str = url
        self._html: str = ""
    async def setHtml(self):
        response = await requests.get(self._url)
        self._html: str = response.text
    def getText(self):
        pass