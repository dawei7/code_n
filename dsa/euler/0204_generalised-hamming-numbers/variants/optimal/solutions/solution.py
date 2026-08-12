def solve(type_n: int = 100, limit: int = 10**9) -> int:
    """Find number of generalised Hamming numbers of type `type_n` <= `limit`.
    
    Time Complexity: O(smooth_count)
    Space Complexity: O(pi(type_n))
    """
    MAX_P = type_n
    is_p = bytearray([1]) * (MAX_P + 1)
    is_p[0] = is_p[1] = 0
    for i in range(2, int(MAX_P**0.5) + 1):
        if is_p[i]:
            is_p[i * i :: i] = b'\x00' * len(is_p[i * i :: i])
    primes = [i for i in range(2, MAX_P + 1) if is_p[i]]

    def dfs(p_idx, val):
        if p_idx == len(primes):
            return 1
        cnt = 0
        p = primes[p_idx]
        v = val
        while v <= limit:
            cnt += dfs(p_idx + 1, v)
            v *= p
        return cnt

    return dfs(0, 1)
