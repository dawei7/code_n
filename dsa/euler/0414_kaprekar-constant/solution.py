"""Project Euler Problem 414: Kaprekar Constant.

Find the last 18 digits of sum_{k=2..300} S(6k+3), where S(b) is the sum of sb(i)
over 0 < i < b^5, and sb(i) is the number of Kaprekar routine steps to reach C_b.
"""

MOD = 10**18


def _s_base(b: int) -> int:
    """Compute S(b) in base b using difference pair (p, q) state graph."""
    t = (b - 3) // 6
    p_star = 4 * t + 2
    q_star = 2 * t + 1

    def idx(p: int, q: int) -> int:
        return (p * (p + 1)) // 2 + q

    size = b * (b + 1) // 2
    target = idx(p_star, q_star)

    nxt = [0] * size
    w = [0] * size

    for p in range(1, b):
        base = (p * (p + 1)) // 2
        bp = b - p

        # q = 0
        c = p - 1
        a = bp
        if c > a:
            mn, mx = a, c
        else:
            mn, mx = c, a
        p2 = b - 1 - mn
        q2 = b - 1 - mx
        nxt[base] = (p2 * (p2 + 1)) // 2 + q2
        w[base] = bp * (20 * p - 10)

        # 1 <= q <= p-1
        for q in range(1, p):
            a1 = p
            a2 = bp
            a3 = q - 1
            a4 = b - q - 1

            if a1 > a2:
                a1, a2 = a2, a1
            if a3 > a4:
                a3, a4 = a4, a3
            if a1 > a3:
                a1, a3 = a3, a1
            if a2 > a4:
                a2, a4 = a4, a2
            if a2 > a3:
                a2, a3 = a3, a2

            p2 = b - 1 - a1
            q2 = a4 - a2
            nxt[base + q] = (p2 * (p2 + 1)) // 2 + q2
            w[base + q] = bp * (120 * q * (p - q) - 20)

        # q = p
        a1 = p
        a2 = bp
        a3 = p - 1
        a4 = b - p - 1

        if a1 > a2:
            a1, a2 = a2, a1
        if a3 > a4:
            a3, a4 = a4, a3
        if a1 > a3:
            a1, a3 = a3, a1
        if a2 > a4:
            a2, a4 = a4, a2
        if a2 > a3:
            a2, a3 = a3, a2

        p2 = b - 1 - a1
        q2 = a4 - a2
        nxt[base + p] = (p2 * (p2 + 1)) // 2 + q2
        w[base + p] = bp * (30 * p - 10)

    dist = [-1] * size
    dist[0] = 0
    dist[target] = 0

    total = 0
    for i in range(1, size):
        if dist[i] != -1:
            continue
        cur = i
        path = []
        while dist[cur] == -1:
            path.append(cur)
            cur = nxt[cur]
        d = dist[cur]
        for node in reversed(path):
            d += 1
            dist[node] = d
            total += w[node] * (d + 1)

    total += w[target] * 1 - 1
    return total % MOD


def solve(k_limit: int = 300) -> str:
    """Compute the last 18 digits of sum_{k=2..k_limit} S(6k+3)."""
    ans = 0
    for k in range(2, k_limit + 1):
        b = 6 * k + 3
        ans = (ans + _s_base(b)) % MOD
    return f"{ans:018d}"


if __name__ == "__main__":
    print(solve())
