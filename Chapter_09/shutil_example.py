import os, shutil

path = r'C:\Users\Luiz Lima\Documents\GitHub\automatetheboringstuff\Chapter_09'
os.chdir(path)
shutil.copy('.\\spam.txt', '.\\delicious') # copies file to location
shutil.copy('eggs.txt', '.\\delicious\\eggs2.txt') # copies and renames file to location
#shutil.copytree('.\\delicious', '.\\delicious_backup') # copies files and dirs to location

for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename) # deletes file at path
        #os.rmdir(path) # deletes empty folder at path
        #shutil.rmtree(path) # deletes folder and its files at path
        print(filename)
