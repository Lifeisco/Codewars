def pig_it(text):
    result = ''
    for word in text.split(' '):
        if word != ',' and word != '.' and word != '!' and word != '?':
            result += word[1:] + word[0] + 'ay' + ' '
        else:
            result += word
    return result.rstrip()

print(pig_it('Quis custodiet ipsos custodes ?'))
