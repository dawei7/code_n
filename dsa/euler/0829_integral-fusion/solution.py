import math

# Tree shape sentinel for prime leaf nodes
_PRIME = 'P'


def solve(limit: int = 31) -> int:
    """Find sum_{n=2}^{31} M(n) for integral fusion factor tree shapes.

    Tree shape bottom-up DP using closest divisor bounds and sorted candidates.

    Time Complexity: O(limit * max_cands^2)
    Space Complexity: O(limit * max_cands)
    """
    def factor_tree(n: int):
        if n <= 1:
            return None
        is_prime = True
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            return _PRIME
        best_a = 1
        best_b = n
        for i in range(math.isqrt(n), 0, -1):
            if n % i == 0:
                best_a = i
                best_b = n // i
                break
        return (factor_tree(best_a), factor_tree(best_b))

    primes = []
    for i in range(2, 5000):
        is_p = True
        for j in range(2, math.isqrt(i) + 1):
            if i % j == 0:
                is_p = False
                break
        if is_p:
            primes.append(i)

    def get_divisors(factors: dict) -> list:
        divs = [1]
        for p, c in factors.items():
            new_divs = []
            for d in divs:
                for i in range(1, c + 1):
                    new_divs.append(d * (p ** i))
            divs.extend(new_divs)
        return divs

    cache = {}

    def get_cands(t, max_cands: int = 300):
        if t in cache:
            return cache[t]
        if t == _PRIME:
            res = []
            for p in primes[:max_cands]:
                res.append((p, {p: 1}))
            cache[t] = res
            return res

        L, R = t
        cands_L = get_cands(L, max_cands)
        cands_R = get_cands(R, max_cands)

        valid = []
        pairs = []
        for val_a, fac_a in cands_L:
            for val_b, fac_b in cands_R:
                if val_a > val_b:
                    continue

                fac_n = {}
                for k, v in fac_a.items():
                    fac_n[k] = fac_n.get(k, 0) + v
                for k, v in fac_b.items():
                    fac_n[k] = fac_n.get(k, 0) + v
                n = val_a * val_b
                pairs.append((n, val_a, val_b, fac_n))

        pairs.sort(key=lambda x: x[0])

        seen = set()
        for n, a, b, fac_n in pairs:
            if n in seen:
                continue

            divs = get_divisors(fac_n)
            divs.sort()

            target = math.isqrt(n)
            best_x = 1
            for d in divs:
                if d <= target:
                    best_x = d
                else:
                    break

            if a == best_x:
                valid.append((n, fac_n))
                seen.add(n)
                if len(valid) >= max_cands:
                    break

        cache[t] = valid
        return valid

    total = 0
    for n in range(2, limit + 1):
        val = 1
        if n % 2 == 0:
            for i in range(2, n + 1, 2):
                val *= i
        else:
            for i in range(3, n + 1, 2):
                val *= i
        t = factor_tree(val)
        
        for max_c in [100, 300, 1000, 3000]:
            cache.clear()
            cands = get_cands(t, max_c)
            if cands:
                total += cands[0][0]
                break

    return total


if __name__ == "__main__":
    print(solve())
