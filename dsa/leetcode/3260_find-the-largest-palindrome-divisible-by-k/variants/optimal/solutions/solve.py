def solve(n: int, k: int) -> str:
    powers = [1] * n
    for exponent in range(1, n):
        powers[exponent] = powers[exponent - 1] * 10 % k

    half_length = (n + 1) // 2
    weights = []
    for index in range(half_length):
        mirrored = n - 1 - index
        weight = powers[mirrored]
        if mirrored != index:
            weight += powers[index]
        weights.append(weight % k)

    reachable = [bytearray(k) for _ in range(half_length + 1)]
    reachable[half_length][0] = 1
    for index in range(half_length - 1, -1, -1):
        weight = weights[index]
        for suffix_remainder in range(k):
            if reachable[index + 1][suffix_remainder]:
                for digit in range(10):
                    reachable[index][(digit * weight + suffix_remainder) % k] = 1

    half = []
    prefix_remainder = 0
    for index, weight in enumerate(weights):
        minimum_digit = 1 if index == 0 else 0
        for digit in range(9, minimum_digit - 1, -1):
            next_remainder = (prefix_remainder + digit * weight) % k
            needed = (-next_remainder) % k
            if reachable[index + 1][needed]:
                half.append(str(digit))
                prefix_remainder = next_remainder
                break

    left = "".join(half)
    return left + left[: n // 2][::-1]
