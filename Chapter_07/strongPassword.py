import re

def check_password(password):
    regex_1 = re.compile(r'[A-Z]+')
    regex_2 = re.compile(r'[a-z]+')
    regex_3 = re.compile(r'[0-9]+')
    regex_4 = re.compile(r'[A-Za-z0-9]{8,}')
    return regex_1.search(password) and regex_2.search(password) and regex_3.search(password) and regex_4.search(password)

if check_password(input('Your password: ')) is not None:
    print('You have a strong password.')
else:
    print('You have a weak password.')
