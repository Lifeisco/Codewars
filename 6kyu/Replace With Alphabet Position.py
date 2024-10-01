def alphabet_position(text):
    result = ''
    alphabet = [chr(i) for i in range(97, 123)]
    for sim in text.lower():
        if sim in alphabet:
            result += f'{alphabet.index(sim)+1} '

    return result.rstrip()

print(alphabet_position('abcdefghigklmnopqrstuvwxyz'))
