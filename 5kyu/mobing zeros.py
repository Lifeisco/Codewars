def move_zeros(lst):
    for el in lst:
        if not el:
            lst.remove(0)
            lst.append(0)

    return lst