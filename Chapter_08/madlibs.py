import re

adjective_regex = re.compile('ADJECTIVE')
noun_regex = re.compile('NOUN')
adverb_regex = re.compile('ADVERB')
verb_regex = re.compile('VERB')

while True:
    try:
        file = open(input('File name: '), 'r+')
        content = file.read()
        break
    except FileNotFoundError:
        print('File not found.')

if adjective_regex.search(content):
    adjective = input('Enter an adjective:\n')
    content = adjective_regex.sub(adjective, content)
if noun_regex.search(content):
    noun = input('Enter a noun:\n')
    content = noun_regex.sub(noun, content)
if adverb_regex.search(content):
    adverb = input('Enter an adverb:\n')
    content = adverb_regex.sub(adverb, content)
if verb_regex.search(content):
    verb = input('Enter a verb:\n')
    content = verb_regex.sub(verb, content)

print(content)
