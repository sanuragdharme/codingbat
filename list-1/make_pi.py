# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
# 
# make_pi() → [3, 1, 4]


def make_pi():
    pi = str(3.14)
    a, b, c = pi[0], pi[2], pi[3]

    pi_list = list()
    pi_list.append(int(a))
    pi_list.append(int(b))
    pi_list.append(int(c))
    return pi_list
