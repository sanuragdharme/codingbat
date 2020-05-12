# Given a string, return a string where for every char in the original, there are two chars.
# 
# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'


def double_char(string):
    new_string = ''

    for i in string:
        new_string += i * 2

    return new_string
