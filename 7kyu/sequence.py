def sequence(x):
    res_list = []
    new_list = []
    for i in range(1, x+1):
        res_list.append(str(i))
    res_list.sort()
    for i in res_list:
        new_list.append(int(i))
    return new_list

print(sequence(15))
