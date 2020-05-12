# Return True if the string "cat" and "dog" appear the same number of times in the given string.
# 
# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True


def cat_dog(string):
    count_cat = 0
    count_dog = 0

    for i in range(len(string)):
        if string[i:i + 3] == "cat":
            count_cat += 1

        if string[i:i + 3] == "dog":
            count_dog += 1

    return count_cat == count_dog
