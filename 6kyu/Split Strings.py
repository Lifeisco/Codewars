def solution(s):
    result = ''
    if len(s) % 2:
        s+='_'
    for i in range(len(s)):
        if i % 2:
            result += f'{s[i-1]}{s[i]} '

    return result.split()


print(solution('abcde'))