"""Project Euler Problem 813: XOR-Powers.

Find P(8^12 * 12^8) modulo 10^9 + 7.
"""

MOD = 1_000_000_007


def xor_product(x: int, y: int) -> int:
    """Carryless multiplication in GF(2)[x]."""
    res = 0
    shift = 0
    while y:
        if y & 1:
            res ^= x << shift
        y >>= 1
        shift += 1
    return res


def xor_pow(base: int, exp: int) -> int:
    """Fast exponentiation under XOR-product."""
    res = 1
    while exp:
        if exp & 1:
            res = xor_product(res, base)
        base = xor_product(base, base)
        exp >>= 1
    return res


def solve(exp: int = pow(8, 12) * pow(12, 8), mod: int = MOD) -> int:
    """Evaluate P(exp) mod mod using Frobenius endomorphism in GF(2)[x]."""
    bit_values = []
    v = 1
    e = exp
    while e:
        if e & 1:
            bit_values.append(v)
        e >>= 1
        v <<= 1

    degs: set[int] = {0}
    for v in bit_values:
        new: set[int] = set()
        for d in degs:
            for add in (0, v, 3 * v):
                nd = d + add
                if nd in new:
                    new.remove(nd)
                else:
                    new.add(nd)
        degs = new

    ans = 0
    for d in degs:
        ans = (ans + pow(2, d, mod)) % mod
    return ans


if __name__ == "__main__":
    print(solve())
