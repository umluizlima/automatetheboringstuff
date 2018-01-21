import os, re

search_regex = re.compile(input('Regular expression: '))

for filename in os.listdir():
    if filename.endswith('.txt'):
        file = open(filename, 'r')
        content = file.readlines()
        for line in content:
            print(search_regex.search(line))
