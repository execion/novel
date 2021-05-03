import requests_async as requests
from bs4 import BeautifulSoup
from .list_chapter.listchapter import ListChapter

class Boxnovel:
    def __init__(self):
        self._html = ""
        self._name = ""
        self._list_chapter = ListChapter()

    async def setNovel(self, url: str):
        response = await requests.get(url)
        self._html = response.text
    
    def getHtml(self) -> str:
        return self._html
    
    def setName(self):
        name = BeautifulSoup(self._html, "lxml").find("h3").text
        self._name = name.rstrip().lstrip()
    
    def getName(self) -> str:
        return self._name
    
    async def setListChapters(self):
        link = BeautifulSoup(self._html, "lxml").find("li", attrs={"class": "wp-manga-chapter"}).a["href"]
        await self._list_chapter.setMenu(link)
