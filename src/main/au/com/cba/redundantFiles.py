import os

from src.main.au.com.cba.util.checksumutil import calculatechecksum


def scanFolders(folder):
    checksum_dict = {}
    for dirName, subdirs, fileList in os.walk(folder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            path = os.path.join(dirName, filename)
            file_hash = calculatechecksum(path)
            if file_hash in checksum_dict:
                checksum_dict[file_hash].append(path)
            else:
                checksum_dict[file_hash] = [path]
    return checksum_dict




def getredundantfilelist(folder):
    checksum_dict = scanFolders(folder)
    dulicate_dict = filterDuplicate(checksum_dict)
    displayduplicates(dulicate_dict)


def displayduplicates(dulicate_dict):
    results = list(filter(lambda x: len(x) > 1, dulicate_dict.values()))
    if len(results) > 0:
        print('Duplicates Found:')
        print('The following files are identical')
        print('___________________')
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
            print('___________________')

    else:
        print('No duplicate files found.')


def filterDuplicate(checksum_dict):
    dulicate_dict = {}
    for key in checksum_dict.keys():
        if key in dulicate_dict:
            dulicate_dict[key] = dulicate_dict[key] + checksum_dict[key]
        else:
            dulicate_dict[key] = checksum_dict[key]
    return dulicate_dict


