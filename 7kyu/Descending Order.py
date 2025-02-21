def descending_order(num):
    num_list = []
    for i in str(num):
        num_list.append(i)
    num_list.sort(reverse=True)
    result = ''
    for k in num_list:
        result += k
    return int(result)

print(descending_order(12345))