def disemvowel(string):
    result = ''
    check = "aeiuoAEIUO"
    for letter in string:
        print(letter)
        if letter not in check:
            result += letter
    return result


print(disemvowel("This website is for losers LOL!"))