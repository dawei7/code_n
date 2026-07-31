def solve(n: int, sick: list[int]) -> int:
    modulus = 1_000_000_007
    healthy = n - len(sick)

    factorial = [1] * (healthy + 1)
    for value in range(1, healthy + 1):
        factorial[value] = factorial[value - 1] * value % modulus

    inverse_factorial = [1] * (healthy + 1)
    inverse_factorial[healthy] = pow(factorial[healthy], modulus - 2, modulus)
    for value in range(healthy, 0, -1):
        inverse_factorial[value - 1] = inverse_factorial[value] * value % modulus

    answer = factorial[healthy]
    answer = answer * inverse_factorial[sick[0]] % modulus
    answer = answer * inverse_factorial[n - 1 - sick[-1]] % modulus

    for left, right in zip(sick, sick[1:]):
        gap = right - left - 1
        answer = answer * inverse_factorial[gap] % modulus
        if gap > 0:
            answer = answer * pow(2, gap - 1, modulus) % modulus

    return answer
