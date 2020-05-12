# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
# 
# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello'


def string_bits(string):
    new_string = ''
    for i in range(len(string)):
        if i % 2 == 0:
            new_string += string[i]

    return new_string
