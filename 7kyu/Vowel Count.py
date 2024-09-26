def get_count(sentence):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    return sum(1 for sim in sentence if sim.lower() in vowel_list)

print(get_count('tRUUe'))
