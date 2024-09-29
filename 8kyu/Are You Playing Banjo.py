def are_you_playing_banjo(name):
    #  does not play banjo
    #  play banjo
    return f'{name} play banjo' if name[0] == 'R' or name[0] == 'r' else f'{name} does not play banjo'

print(are_you_playing_banjo('Artur'))
print(are_you_playing_banjo('Robert'))
