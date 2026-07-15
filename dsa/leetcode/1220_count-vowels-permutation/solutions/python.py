MODULUS = 1_000_000_007


def solve(n: int) -> int:
    a = e = i = o = u = 1
    for _ in range(1, n):
        a, e, i, o, u = (
            (e + i + u) % MODULUS,
            (a + i) % MODULUS,
            (e + o) % MODULUS,
            i,
            (i + o) % MODULUS,
        )
    return (a + e + i + o + u) % MODULUS
