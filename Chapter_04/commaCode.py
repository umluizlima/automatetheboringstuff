def code(list):
    string = ''
    for i in range(len(list)):
        if i == len(list) - 1:
            string += 'and ' + list[i]
        else:
            string += list[i] + ', '
    return string

spam = ['apples', 'bananas', 'tofu', 'cats']
print(code(spam))
