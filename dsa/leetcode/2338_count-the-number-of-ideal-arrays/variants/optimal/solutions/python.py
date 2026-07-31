MOD = 1_000_000_007


def solve(n: int, maxValue: int) -> int:
    max_exponent = maxValue.bit_length() - 1
    combinations = [1] * (max_exponent + 1)
    inverses = [0] * (max_exponent + 1)
    if max_exponent >= 1:
        inverses[1] = 1
    for exponent in range(1, max_exponent + 1):
        if exponent > 1:
            inverses[exponent] = (
                MOD - (MOD // exponent) * inverses[MOD % exponent] % MOD
            )
        combinations[exponent] = (
            combinations[exponent - 1]
            * (n + exponent - 1)
            % MOD
            * inverses[exponent]
            % MOD
        )

    smallest_prime = [0] * (maxValue + 1)
    for value in range(2, maxValue + 1):
        if smallest_prime[value] != 0:
            continue
        smallest_prime[value] = value
        if value * value <= maxValue:
            for multiple in range(value * value, maxValue + 1, value):
                if smallest_prime[multiple] == 0:
                    smallest_prime[multiple] = value

    answer = 0
    for final_value in range(1, maxValue + 1):
        ways = 1
        remaining = final_value
        while remaining > 1:
            prime = smallest_prime[remaining]
            exponent = 0
            while remaining % prime == 0:
                remaining //= prime
                exponent += 1
            ways = ways * combinations[exponent] % MOD
        answer = (answer + ways) % MOD

    return answer
