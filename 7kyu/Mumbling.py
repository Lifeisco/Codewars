def accum(st):
    result = ''
    for i, let in enumerate(st):
        if i + 1 == len(st):
            result += f'{(let * (i+1)).capitalize()}'
            break
        result += f'{(let*(i+1)).capitalize()}-'
    return result

print(accum("Zpgl"))
print(accum("ZpglnRxqenU"))


'''
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
'''