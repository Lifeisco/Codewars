def high_and_low(numbers):
    num_list = numbers.split()
    result = list(map(int, num_list))

    return f'{max(result)} {min(result)}'


print(high_and_low('8 3 -5 42 -1 0 0 -9 4 7 4 -4'))