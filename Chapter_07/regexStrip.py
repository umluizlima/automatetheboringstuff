import re

def regex_strip(s, c = ''):
    if c == '':
        c = r'^\s*|\s*$'
    strip_regex = re.compile(c)
    return strip_regex.sub('', s)

print(regex_strip(input('String: '), input('Char: ')))
        
