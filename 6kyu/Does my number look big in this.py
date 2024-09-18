def narcissistic(value):
    num_list = []
    sum_result = 0
    for num in str(value):
        num_list.append(num)
        sum_result += int(num) ** len(str(value))
    if sum_result == value:
        return True
    else:
        return False
