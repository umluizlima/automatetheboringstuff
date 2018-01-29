#! python3
# fillingInTheGaps - a program that finds all files with a given prefix in a single folder
# and locates any gaps in the numbering, renaming later files to close it.

import os, re, shutil

prefix = re.compile(r'spam(\d{3}).txt')
num = re.compile(r'\d{3}')

def fillingInTheGaps(src):
    src = os.path.abspath(src)
    numbers = list()
    for filename in os.listdir(src):
        if len(prefix.findall(filename)):
            numbers.append(prefix.findall(filename)[0])
            if int(numbers[-1]) != len(numbers):
                os.rename(os.path.join(src, filename),
                          os.path.join(src, num.sub('{0:03d}'.format(len(numbers)), filename)))
                print(num.sub('{0:03d}'.format(len(numbers)), filename))
                
fillingInTheGaps(r'.')
