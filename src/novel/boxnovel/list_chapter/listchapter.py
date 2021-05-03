from bs4 import BeautifulSoup
import requests_async as requests
from .chapter.chapter import Chapter

class ListChapter:
    def __init__(self):
        self._listChapters = []
    
    async def setMenu(self, url: str):
        response = await requests.get(url)
        html = response.text
        list_temp = BeautifulSoup(html, "lxml").findAll("option")
        list_temp = list(set(list_temp))
        self._listChapters = [chapter["data-redirect"] for chapter in list_temp]
        print(self._listChapters)
    
    async def getChapter(self):
        for url in self._listChapters:
            chapter = Chapter(url=url)
            await chapter.setHtml()
