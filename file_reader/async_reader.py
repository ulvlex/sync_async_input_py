import argparse
import time
import datetime
import aiofiles
import asyncio
import os

async def readFile(filename):
    async with aiofiles.open(filename, mode='rb') as f:
        print(filename)
        while True:
            #time.sleep(0.001)
            data = await f.read()
            if not data:
                print(filename, "done ###############")
                return True
                break

def readFilesInDirectory(directory):
    listOfFiles = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filePath = os.path.join(root, filename)
            if os.path.isfile(filePath):
                listOfFiles.append(filePath)
    return listOfFiles

def createParserArg():
    parser = argparse.ArgumentParser(description='Read files in a directory')
    parser.add_argument('directory', type=str, help='Path to the directory to read files from')

    return parser
async def main():
    begin = datetime.datetime.now() #считываем время

    parser = createParserArg()
    args = parser.parse_args()
    directory = args.directory

    #список аргументов для readFile()
    listOfFiles = readFilesInDirectory(directory)
    print(listOfFiles)

    #создаём задачи
    tasks = [asyncio.create_task(readFile(file)) for file in listOfFiles]

    #передаём задачи в функцию as_completed()
    for future in asyncio.as_completed(tasks):
        #получаем результат по готовности
        await future

    print(datetime.datetime.now() - begin)

asyncio.run(main())