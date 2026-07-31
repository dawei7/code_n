def solve(n: int, m: int, k: int) -> int:
    modulo = 1_000_000_007
    slots = n - 1
    selected = min(k, slots - k)

    numerator = 1
    denominator = 1
    for value in range(1, selected + 1):
        numerator = numerator * (slots - selected + value) % modulo
        denominator = denominator * value % modulo

    combinations = numerator * pow(denominator, modulo - 2, modulo) % modulo
    changes = slots - k
    return m * combinations % modulo * pow(m - 1, changes, modulo) % modulo
