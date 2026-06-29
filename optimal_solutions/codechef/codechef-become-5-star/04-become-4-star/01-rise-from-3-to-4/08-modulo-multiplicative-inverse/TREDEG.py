import sys
MOD = 998244353
ROOT = 3

def ntt(a: list[int], invert: bool) -> None:
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = (a[j], a[i])
    length = 2
    while length <= n:
        wlen = pow(ROOT, (MOD - 1) // length, MOD)
        if invert:
            wlen = pow(wlen, MOD - 2, MOD)
        half = length >> 1
        for i in range(0, n, length):
            w = 1
            end = i + half
            for j in range(i, end):
                u = a[j]
                v = a[j + half] * w % MOD
                x = u + v
                if x >= MOD:
                    x -= MOD
                y = u - v
                if y < 0:
                    y += MOD
                a[j] = x
                a[j + half] = y
                w = w * wlen % MOD
        length <<= 1
    if invert:
        inv_n = pow(n, MOD - 2, MOD)
        for i in range(n):
            a[i] = a[i] * inv_n % MOD

def convolution(a: list[int], b: list[int], limit: int) -> list[int]:
    if not a or not b or limit <= 0:
        return []
    need = min(limit, len(a) + len(b) - 1)
    if min(len(a), len(b)) <= 32:
        out = [0] * need
        if len(a) < len(b):
            for i, ai in enumerate(a):
                if ai:
                    upto = min(len(b), need - i)
                    for j in range(upto):
                        out[i + j] = (out[i + j] + ai * b[j]) % MOD
        else:
            for i, bi in enumerate(b):
                if bi:
                    upto = min(len(a), need - i)
                    for j in range(upto):
                        out[i + j] = (out[i + j] + bi * a[j]) % MOD
        return out
    size = 1
    while size < len(a) + len(b) - 1:
        size <<= 1
    fa = a[:] + [0] * (size - len(a))
    fb = b[:] + [0] * (size - len(b))
    ntt(fa, False)
    ntt(fb, False)
    for i in range(size):
        fa[i] = fa[i] * fb[i] % MOD
    ntt(fa, True)
    return fa[:need]

def poly_inv(a: list[int], n: int) -> list[int]:
    result = [pow(a[0], MOD - 2, MOD)]
    length = 1
    while length < n:
        length <<= 1
        current = a[:length]
        prod = convolution(current, result, length)
        for i in range(len(prod)):
            prod[i] = -prod[i] % MOD
        prod[0] = (prod[0] + 2) % MOD
        result = convolution(result, prod, length)
    return result[:n]

def poly_derivative(a: list[int]) -> list[int]:
    return [a[i] * i % MOD for i in range(1, len(a))]

def poly_integral(a: list[int], inv: list[int], n: int) -> list[int]:
    out = [0] * n
    upto = min(len(a), n - 1)
    for i in range(upto):
        out[i + 1] = a[i] * inv[i + 1] % MOD
    return out

def poly_log(a: list[int], n: int, inv: list[int]) -> list[int]:
    derivative = poly_derivative(a)
    inverse = poly_inv(a, n)
    product = convolution(derivative, inverse, n - 1)
    return poly_integral(product, inv, n)

def poly_exp(a: list[int], n: int, inv: list[int]) -> list[int]:
    result = [1]
    length = 1
    while length < n:
        length <<= 1
        log_result = poly_log(result, length, inv)
        correction = [0] * length
        upto = min(length, len(a))
        for i in range(upto):
            correction[i] = a[i]
        for i in range(length):
            correction[i] = (correction[i] - log_result[i]) % MOD
        correction[0] = (correction[0] + 1) % MOD
        result = convolution(result, correction, length)
    return result[:n]

def coefficient_power_for_small_n(n: int, k: int, fact: list[int], invfact: list[int], inv: list[int]) -> int:
    length = n - 1
    prufer = n - 2
    f = [0] * length
    for i in range(length):
        f[i] = pow(i + 1, k, MOD) * invfact[i] % MOD
    log_f = poly_log(f, length, inv)
    for i in range(length):
        log_f[i] = log_f[i] * n % MOD
    powered = poly_exp(log_f, length, inv)
    coefficient = powered[prufer]
    return fact[prufer] * coefficient % MOD * pow(pow(n, prufer, MOD), MOD - 2, MOD) % MOD

def answer_k_one(n: int, fact: list[int], invfact: list[int]) -> int:
    prufer = n - 2
    if prufer == 0:
        return 1
    inv_n = pow(n, MOD - 2, MOD)
    power_n = pow(n, prufer, MOD)
    choose_factor = fact[n]
    total = 0
    current_power = power_n
    for j in range(prufer + 1):
        comb = choose_factor * invfact[j] % MOD * invfact[n - j] % MOD
        total = (total + comb * current_power % MOD * invfact[prufer - j]) % MOD
        current_power = current_power * inv_n % MOD
    return fact[prufer] * total % MOD * pow(power_n, MOD - 2, MOD) % MOD

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    test_count = data[0]
    pairs = [(data[i], data[i + 1]) for i in range(1, len(data), 2)]
    max_n = max((n for n, _ in pairs))
    inverse_limit = 1
    while inverse_limit < max_n + 1:
        inverse_limit <<= 1
    fact = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fact[i] = fact[i - 1] * i % MOD
    invfact = [1] * (max_n + 1)
    invfact[max_n] = pow(fact[max_n], MOD - 2, MOD)
    for i in range(max_n, 0, -1):
        invfact[i - 1] = invfact[i] * i % MOD
    inv = [0] * (inverse_limit + 1)
    if inverse_limit >= 1:
        inv[1] = 1
    for i in range(2, inverse_limit + 1):
        inv[i] = (MOD - MOD // i) * inv[MOD % i] % MOD
    output = []
    for n, k in pairs[:test_count]:
        if k == 1:
            output.append(str(answer_k_one(n, fact, invfact)))
        else:
            output.append(str(coefficient_power_for_small_n(n, k, fact, invfact, inv)))
    sys.stdout.write('\n'.join(output))


if __name__ == "__main__":
    solve()
