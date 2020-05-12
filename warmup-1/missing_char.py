# Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of
# n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(string)-1 inclusive).
# 
# missing_char('kitten', 1) → 'ktten'
# missing_char('kitten', 0) → 'itten'
# missing_char('kitten', 4) → 'kittn'


def missing_char(string, n):
    front = string[:n]
    back = string[n + 1:]
    return front + back
