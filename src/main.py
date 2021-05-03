import asyncio
from novel.boxnovel import Boxnovel

async def main():
    boxnovel = Boxnovel()
    await boxnovel.setNovel("https://boxnovel.com/novel/super-gene-optimization-fluid/")
    boxnovel.setName()
    await boxnovel.setListChapters()

asyncio.run(main())