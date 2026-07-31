from collections import Counter


def solve(s: str) -> int:
    modulus = 1_000_000_007
    frequencies = Counter(s)
    length = len(s)

    factorial = [1] * (length + 1)
    for value in range(1, length + 1):
        factorial[value] = factorial[value - 1] * value % modulus

    inverse_factorial = [1] * (length + 1)
    inverse_factorial[length] = pow(factorial[length], modulus - 2, modulus)
    for value in range(length, 0, -1):
        inverse_factorial[value - 1] = inverse_factorial[value] * value % modulus

    answer = 0
    for chosen_frequency in range(1, max(frequencies.values()) + 1):
        ways = 1
        for frequency in frequencies.values():
            if frequency < chosen_frequency:
                continue
            combinations = (
                factorial[frequency]
                * inverse_factorial[chosen_frequency]
                * inverse_factorial[frequency - chosen_frequency]
                % modulus
            )
            ways = ways * (combinations + 1) % modulus
        answer = (answer + ways - 1) % modulus

    return answer
