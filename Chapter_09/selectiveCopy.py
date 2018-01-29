#! python3
# selectiveCopy - a program that walks through a folder tree and searches for
# files with a certain file extension, copying them into a new folder.

import os, shutil

def selectiveCopy(src, dst, ext):
    src = os.path.abspath(src)
    dst = os.path.abspath(dst)
    ext = ext.lower()
    for foldername, subfolders, filenames in os.walk(src):
        #print(str(foldername) + '\n' + str(subfolders) + '\n' + str(filenames))
        for filename in filenames:
            if os.path.splitext(filename)[1].lower() == ext:
                shutil.copy(os.path.join(foldername, filename), os.path.join(dst, filename))
                
print('This program walks through the source folder tree and copies files with given file extension into destination folder')
src = input('Source folder: ')
dst = input('Destination folder: ')
ext = input('File extension: ')
selectiveCopy(src, dst, ext)
