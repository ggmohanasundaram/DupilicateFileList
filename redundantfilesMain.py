import os
import sys

from src.main.au.com.cba.redundantFiles import getredundantfilelist

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_folders = sys.argv[1:]
        for folder in input_folders:
            if os.path.exists(folder):
                getredundantfilelist(folder)
            else:
                print('%s is not a valid path, please verify' % folder)
                sys.exit()

    else:
        print('Usage: python redundantFiles.py <folderName> or python redundantFiles.py <folderName1> <folderName2> ')
