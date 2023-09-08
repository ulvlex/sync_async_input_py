import aiofiles
import asyncio
import datetime

async def read_file(filename):
    pass # to-do

async def main():
    begin = datetime.datetime.now()
    files = ['/home/sia/tmp/{}'.format(i) for i in range(1, 11)]
    #to-do use asyncio.as_completed to call read_file

    print(datetime.datetime.now() - begin)

asyncio.run(main())
