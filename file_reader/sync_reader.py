import argparse #for command line input
import datetime
import time
import os

def readFile(filename):
    with open(filename, mode='rb') as f:
        print(filename)
        while True:
            #time.sleep(0.001)
            data = f.read(1024)
            if not data:
                print(filename, "done ###############")
                break

def readFilesInDirectory(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filePath = os.path.join(root, filename)
            if os.path.isfile(filePath):
                readFile(filePath)
def createParserArg():
    parser = argparse.ArgumentParser(description='Read files in a directory')
    parser.add_argument('directory', type=str, help='Path to the directory to read files from')

    return parser
def main():
    begin = datetime.datetime.now()

    parser = createParserArg()
    args = parser.parse_args()
    directory = args.directory

    readFilesInDirectory(directory)
    print(datetime.datetime.now() - begin)

if __name__ == "__main__":
    main()