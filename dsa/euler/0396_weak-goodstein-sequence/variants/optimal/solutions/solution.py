"""Project Euler Problem 396: Weak Goodstein Sequence.

Find the last 9 digits of sum_{1 <= n < 16} G(n), where G(n) is the number of non-zero terms
in the nth weak Goodstein sequence.
"""

from typing import List, Optional, Tuple

MOD = 1_000_000_000
MOD2 = 1 << 9  # 512
MOD5 = 5**9  # 1953125


def _egcd(a: int, b: int) -> Tuple[int, int, int]:
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def _inv_mod(a: int, m: int) -> int:
    a %= m
    g, x, _ = _egcd(a, m)
    if g != 1:
        raise ValueError("inverse does not exist")
    return x % m


def _factor_2_5(n_val: int) -> Tuple[int, int]:
    a = b = 0
    tmp = n_val
    while tmp % 2 == 0:
        tmp //= 2
        a += 1
    while tmp % 5 == 0:
        tmp //= 5
        b += 1
    return a, b


def _phi_2_5(n_val: int) -> int:
    if n_val == 1:
        return 1
    a, b = _factor_2_5(n_val)
    phi2 = 1 if a <= 1 else (1 << (a - 1))
    phi5 = 1 if b == 0 else (4 * (5 ** (b - 1)))
    return phi2 * phi5


def _phi_chain(mod0: int) -> List[int]:
    mods = [mod0]
    while mods[-1] != 1:
        mods.append(_phi_2_5(mods[-1]))
    return mods


def _f2_exact(x: int) -> int:
    return (x + 1) * (1 << (x + 1)) - 1


def _a_exact_upto7(n_val: int) -> int:
    b0 = n_val & 1
    b1 = (n_val >> 1) & 1
    b2 = (n_val >> 2) & 1
    x = 2 + b0
    if b1:
        x = 2 * x + 1
    if b2:
        x = _f2_exact(x)
    return x


_INV_MOD2_MOD5 = _inv_mod(MOD2 % MOD5, MOD5)


def _crt_1e9(r2: int, r5: int) -> int:
    t = ((r5 - r2) % MOD5) * _INV_MOD2_MOD5 % MOD5
    return (r2 + MOD2 * t) % MOD


class _ChainInfo:
    __slots__ = ("mod", "a2", "b5", "m2", "m5", "phi5", "inv_m5_mod_m2")

    def __init__(self, mod: int):
        self.mod = mod
        if mod == 1:
            self.a2 = self.b5 = 0
            self.m2 = self.m5 = 1
            self.phi5 = 1
            self.inv_m5_mod_m2 = 0
            return

        a2, b5 = _factor_2_5(mod)
        self.a2, self.b5 = a2, b5
        self.m2 = 1 << a2 if a2 else 1
        self.m5 = 5**b5 if b5 else 1
        self.phi5 = 4 * (5 ** (b5 - 1)) if b5 else 1
        self.inv_m5_mod_m2 = (
            _inv_mod(self.m5 % self.m2, self.m2) if (a2 and b5) else 0
        )


_CHAIN5 = [_ChainInfo(m) for m in _phi_chain(MOD5)]


def _pow2_mod_chain_level(
    info: _ChainInfo, next_res: int, exact_x: Optional[int]
) -> int:
    m = info.mod
    if m == 1:
        return 0

    if info.a2:
        r2 = (
            (1 << (exact_x + 1))
            if (exact_x is not None and (exact_x + 1) < info.a2)
            else 0
        )
    else:
        r2 = 0

    if info.b5:
        exp_mod = (next_res % info.phi5 + 1) % info.phi5
        r5 = pow(2, exp_mod, info.m5)
    else:
        r5 = 0

    if info.a2 == 0:
        return r5
    if info.b5 == 0:
        return r2

    m2 = info.m2
    mask = m2 - 1
    t = (((r2 - r5) & mask) * info.inv_m5_mod_m2) & mask
    return (r5 + info.m5 * t) % m


def _f2_iter_mod5(x0: int, iters: int) -> int:
    residues = [x0 % info.mod for info in _CHAIN5]
    exact_x: Optional[int] = x0 if x0 <= 20 else None

    for _ in range(iters):
        new_res = [0] * len(residues)
        exact_x_next = (
            _f2_exact(exact_x)
            if (exact_x is not None and _f2_exact(exact_x) <= 20)
            else None
        )

        for i, info in enumerate(_CHAIN5):
            m = info.mod
            if m == 1:
                new_res[i] = 0
                continue
            next_res = residues[i + 1]
            p2 = _pow2_mod_chain_level(info, next_res, exact_x)
            new_res[i] = (((residues[i] + 1) % m) * p2 - 1) % m

        residues = new_res
        exact_x = exact_x_next

    return residues[0]


def _f2_iter_mod2(x0: int, iters: int) -> int:
    mask = MOD2 - 1
    x_mod = x0 & mask
    exact_x: Optional[int] = x0 if x0 <= 20 else None

    for _ in range(iters):
        if exact_x is not None and (exact_x + 1) < 9:
            p2 = 1 << (exact_x + 1)
            exact_next = _f2_exact(exact_x)
            exact_x = exact_next if exact_next <= 20 else None
        else:
            p2 = 0
            exact_x = None
        x_mod = (((x_mod + 1) & mask) * p2 - 1) & mask

    return x_mod


def _a_mod(n_val: int, a0_7: List[int]) -> int:
    if n_val < 8:
        return a0_7[n_val]
    x0 = a0_7[n_val - 8]
    iters = x0 + 1
    r5 = _f2_iter_mod5(x0, iters)
    r2 = _f2_iter_mod2(x0, iters)
    return _crt_1e9(r2, r5)


def solve() -> str:
    """Compute the last 9 digits of sum_{1 <= n < 16} G(n)."""
    a0_7 = [_a_exact_upto7(n) for n in range(8)]
    a_mods = [_a_mod(n, a0_7) for n in range(16)]

    total = 0
    for n in range(1, 16):
        total = (total + (a_mods[n] - 2)) % MOD

    return f"{total:09d}"


if __name__ == "__main__":
    print(solve())
