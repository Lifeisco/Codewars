def make_readable(seconds):
    HH = seconds//3600
    MM = (seconds % 3600) // 60 if seconds % 3600 >= 60 else 0
    SS = (seconds % 3600) % 60

    return f'{"0" + str(HH) if HH < 10 else HH}:{"0" + str(MM) if MM < 10 else MM}:{"0" + str(SS) if SS < 10 else SS}'

print(make_readable(32))
