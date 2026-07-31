from collections import Counter


def solve(s):
    modulus = 1_000_000_007
    words = s.split()
    maximum_length = max(map(len, words))

    factorial = [1] * (maximum_length + 1)
    for value in range(1, maximum_length + 1):
        factorial[value] = factorial[value - 1] * value % modulus

    inverse_factorial = [1] * (maximum_length + 1)
    inverse_factorial[maximum_length] = pow(
        factorial[maximum_length], modulus - 2, modulus
    )
    for value in range(maximum_length, 0, -1):
        inverse_factorial[value - 1] = inverse_factorial[value] * value % modulus

    answer = 1
    for word in words:
        ways = factorial[len(word)]
        for frequency in Counter(word).values():
            ways = ways * inverse_factorial[frequency] % modulus
        answer = answer * ways % modulus

    return answer
