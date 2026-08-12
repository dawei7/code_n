import math


def solve_S(n: int) -> int:
    row_starts = [((r - 1) * r // 2 + 1) for r in range(n - 2, n + 3)]
    row_lens = [r for r in range(n - 2, n + 3)]

    min_val = row_starts[0]
    max_val = row_starts[4] + row_lens[4] - 1
    segment_len = max_val - min_val + 1

    max_prime = int(math.isqrt(max_val)) + 1

    is_p = bytearray([1]) * (max_prime + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(max_prime**0.5) + 1):
        if is_p[i]:
            is_p[i * i :: i] = b'\x00' * len(is_p[i * i :: i])
    primes = [i for i in range(2, max_prime + 1) if is_p[i]]

    is_prime_seg = bytearray([1]) * segment_len
    for p in primes:
        start = ((min_val + p - 1) // p) * p
        if start < p * p:
            start = p * p
        if start <= max_val:
            is_prime_seg[start - min_val :: p] = b'\x00' * len(
                is_prime_seg[start - min_val :: p]
            )

    def is_p_rc(r_idx, c):
        if c < 1 or c > row_lens[r_idx]:
            return False
        val = row_starts[r_idx] + c - 1
        return is_prime_seg[val - min_val] == 1

    def get_prime_neighbors(r_idx, c):
        res = 0
        if r_idx > 0:
            if is_p_rc(r_idx - 1, c - 1):
                res += 1
            if is_p_rc(r_idx - 1, c):
                res += 1
            if is_p_rc(r_idx - 1, c + 1):
                res += 1
        if is_p_rc(r_idx, c - 1):
            res += 1
        if is_p_rc(r_idx, c + 1):
            res += 1
        if r_idx < 4:
            if is_p_rc(r_idx + 1, c - 1):
                res += 1
            if is_p_rc(r_idx + 1, c):
                res += 1
            if is_p_rc(r_idx + 1, c + 1):
                res += 1
        return res

    n_count = {}
    for r_idx in range(1, 4):
        for c in range(1, row_lens[r_idx] + 1):
            if is_p_rc(r_idx, c):
                n_count[(r_idx, c)] = get_prime_neighbors(r_idx, c)

    total = 0
    for c in range(1, row_lens[2] + 1):
        if is_p_rc(2, c):
            val = row_starts[2] + c - 1
            if n_count.get((2, c), 0) >= 2:
                total += val
            else:
                neighbors = []
                if is_p_rc(1, c - 1):
                    neighbors.append((1, c - 1))
                if is_p_rc(1, c):
                    neighbors.append((1, c))
                if is_p_rc(1, c + 1):
                    neighbors.append((1, c + 1))
                if is_p_rc(2, c - 1):
                    neighbors.append((2, c - 1))
                if is_p_rc(2, c + 1):
                    neighbors.append((2, c + 1))
                if is_p_rc(3, c - 1):
                    neighbors.append((3, c - 1))
                if is_p_rc(3, c):
                    neighbors.append((3, c))
                if is_p_rc(3, c + 1):
                    neighbors.append((3, c + 1))

                if any(n_count.get(nb, 0) >= 2 for nb in neighbors):
                    total += val

    return total


def solve(n1: int = 5678027, n2: int = 7208785) -> int:
    """Find S(n1) + S(n2) for Prime Triplets.
    
    Time Complexity: O(n1 + n2)
    Space Complexity: O(n1 + n2)
    """
    return solve_S(n1) + solve_S(n2)
