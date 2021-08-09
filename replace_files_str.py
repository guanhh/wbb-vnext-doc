import os
import re

def listFiles(dirPath, suffix):
    fileList = []
    for root, dirs, files in os.walk(dirPath):
        for fileObj in files:
            if fileObj.endswith(suffix):
                print(fileObj)
                fileList.append(os.path.join(root, fileObj))
    return fileList


def main():
    fileList = listFiles('D:\File\Test\github\wbb_doc_site', '.html')
    print(fileList)

    for fileObj in fileList:
        with open(fileObj, 'r+', encoding='utf-8') as f:

            all_the_lines = f.readlines()
            f.seek(0)
            f.truncate()

            for line in all_the_lines:
                f.write(line.replace('/images/', 'https://raw.githubusercontent.com/guanhh/wbb-vnext-doc/main/images/'))

            print(fileObj+'：替换完成')


if __name__ == '__main__':
    main()