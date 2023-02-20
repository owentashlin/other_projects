def filter_list(l):
    filter_list = []
    for x in l:
        if type(x) == int:
            filter_list.append(x)
    return filter_list


def is_divisible(n,x,y):
    if ((n % x == 0) and (n % y == 0)):
        return True
    else:
        return False