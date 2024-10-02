def tribonacci(signature, n):
    result = signature

    if n > 3:
        for num in range(n - 3):
            result.append(sum(signature[:-4:-1]))

        return result
    else:
        return signature[:n]


for i in range(0, 5):
    print(tribonacci([1, 2, 3], i))