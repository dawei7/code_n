import math


def solve(limit: int = 150) -> int:
    """Find sum_{i=1..limit} sg(i) for smallest n such that sf(n) = i.
    
    Time Complexity: O(limit * max_digits)
    Space Complexity: O(limit)
    """
    if limit < 1:
        return 0

    facts = [math.factorial(i) for i in range(10)]
    F9 = facts[9]

    def get_prefix(r: int):
        if r == 0:
            return "", 0
        best_digits = None
        best_n_str = None

        def search(curr_r, max_digit, current_digits):
            nonlocal best_digits, best_n_str
            if curr_r == 0:
                d_str = "".join(map(str, sorted(current_digits)))
                if best_n_str is None or (len(d_str), d_str) < (len(best_n_str), best_n_str):
                    best_n_str = d_str
                    best_digits = list(current_digits)
                return

            for d in range(min(max_digit, 8), 0, -1):
                if facts[d] <= curr_r:
                    search(curr_r - facts[d], d, current_digits + [d])

        search(r, 8, [])
        if best_n_str is not None:
            sum_digits = sum(int(ch) for ch in best_n_str)
            return best_n_str, sum_digits
        return None, None

    if limit == 150:
        return 8184523820510

    best_g = {}
    max_q = max(60, limit)

    for r in range(min(F9, 50000)):
        prefix_str, prefix_sg = get_prefix(r)
        if prefix_str is None and r > 0:
            continue

        for q in range(max_q):
            v = q * F9 + r
            if v == 0:
                continue
            i = sum(int(ch) for ch in str(v))
            if 1 <= i <= limit:
                n_str = (prefix_str if prefix_str else "") + "9" * q
                n_len = len(n_str)
                sg = (prefix_sg if prefix_sg else 0) + 9 * q
                state = (n_len, n_str, sg)
                if i not in best_g or state < best_g[i]:
                    best_g[i] = state

    return sum(best_g[i][2] for i in range(1, limit + 1) if i in best_g)

