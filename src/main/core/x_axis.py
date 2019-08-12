
def is_overlaped(line_one, line_two):
    set_one = set(range(line_one[0], line_one[1]))
    set_two = set(range(line_two[0], line_two[1]))

    if len(set_one.intersection(set_two)) >0:
        return True
    else:
        return False


print(is_overlaped((1, 5), (6, 8)))
