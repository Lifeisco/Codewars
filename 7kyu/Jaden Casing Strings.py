def to_jaden_case(string):
    res = [f'{word.capitalize()} ' for word in string.split()]
    return ''.join(res).strip()

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))