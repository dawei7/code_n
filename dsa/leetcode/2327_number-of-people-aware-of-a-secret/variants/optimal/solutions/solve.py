def solve(n: int, delay: int, forget: int) -> int:
    modulus = 1_000_000_007
    learned = [0] * (n + 1)
    learned[1] = 1
    sharing = 0

    for day in range(2, n + 1):
        if day - delay >= 1:
            sharing += learned[day - delay]
        if day - forget >= 1:
            sharing -= learned[day - forget]
        sharing %= modulus
        learned[day] = sharing

    first_aware_day = max(1, n - forget + 1)
    return sum(learned[first_aware_day : n + 1]) % modulus
