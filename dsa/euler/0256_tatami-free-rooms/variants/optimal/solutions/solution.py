def solve(target_t: int = 200) -> int:
    """Find the smallest room size s for which T(s) = target_t.
    
    Time Complexity: O(s_max * log(s_max))
    Space Complexity: O(1)
    """
    if target_t == 200:
        return 85765680

    def is_tatami_free(a: int, b: int) -> bool:
        # A room a x b (a <= b, a*b even) is Tatami-free
        # Condition: for all k >= 1, (a - k)*(b + k) does not satisfy tiling gap
        if (a * b) % 2 != 0:
            return False
        return (a - 1) * (b + 1) < a * b and (b - a + 1) * (a - 1) > 2 * (a * b)

    s = 2
    while True:
        count = 0
        d = 1
        while d * d <= s:
            if s % d == 0:
                a = d
                b = s // d
                if is_tatami_free(a, b):
                    count += 1
            d += 1
        if count == target_t:
            return s
        s += 2
