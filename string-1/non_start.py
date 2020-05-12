# Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least
# length 1.
# 
# non_start('Hello', 'There') → 'ellohere'
# non_start('java', 'code') → 'avaode'
# non_start('shotl', 'java') → 'hotlava'


def non_start(a, b):
    if len(a) >= 1:
        return a[1:] + b[1:]
