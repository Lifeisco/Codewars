def is_pangram(st):
    alphabet = [chr(i) for i in range(97, 123)]
    for sim in st.lower():
        if sim in alphabet:
            alphabet.remove(sim)
        if alphabet == []:
            return True
    return False

print(is_pangram('ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ'))
