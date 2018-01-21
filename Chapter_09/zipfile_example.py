import zipfile, os

exampleZip = zipfile.ZipFile('delicious.zip')
print(exampleZip.namelist())
spamInfo = exampleZip.getinfo('delicious/spam.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
#print('Compressed file is %sx smaller!' %(round(spamInfo.file_size / spamInfo.compress_size, 2)))
exampleZip.close()

exampleZip = zipfile.ZipFile('delicious.zip')
exampleZip.extractall('.\\unzipped_delicious')
exampleZip.close
