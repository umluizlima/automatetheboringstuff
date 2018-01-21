#! python3
#bulletPointAdder.py - Adds Wikipedia bullet points to the start
#of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()

# TODO: Separate lines and add stars.
lines = text.split('\n')
print(lines)
for i in range(len(lines)):
    if not lines[i] == '':
        lines[i] = '* ' + lines[i]
text = '\n'.join(lines)

print(text)

pyperclip.copy(text)
