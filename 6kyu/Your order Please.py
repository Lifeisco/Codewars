def order(sentence):
    result = []
    word_list = sentence.split(' ')
    num_dict = []
    dict = {}
    pre_list = []
    for i in range(1, 10):
        num_dict.append(f'{i}')

    for word in word_list:
        for simbol in word:
            if simbol in num_dict:
                result.append(int(simbol))
                dict[int(simbol)] = word

    result.sort()
    for item in result:
        pre_list.append(dict[item])

    return ' '.join(pre_list)
