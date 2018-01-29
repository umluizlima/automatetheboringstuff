#! python3
# deletingUnneededFiles - a program that walks through a folder tree and searches for
# exceptionally large files or folders (over 100MB)

import os, shutil

def deletingUnneededFiles(src):
    src = os.path.abspath(src)
    for foldername, subfolders, filenames in os.walk(src):
        for subfolder in subfolders:
            if os.path.getsize(os.path.join(foldername, subfolder)) >= 100000000:
                print('Folder:', subfolder, 'is larger than 100MB')
        for filename in filenames:
            if os.path.getsize(os.path.join(foldername, filename)) >= 100000000:
                print('File:', filename, 'is larger than 100MB')

deletingUnneededFiles(r'C:\\Users\\Luiz Lima\\Downloads')
            
