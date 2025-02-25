def is_square(n):
    if n >= 0:
        return (n ** 0.5).is_integer()
    else:
        return False


print(is_square(15))
print(is_square(25))
print(is_square(-1))
print(is_square(0))
print(is_square(1))