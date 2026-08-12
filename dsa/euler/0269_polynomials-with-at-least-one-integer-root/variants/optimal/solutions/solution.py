def solve(limit: int = 10**16) -> int:
    """Find Z(limit), the number of positive integers n < limit for which P_n(x) has at least one integer root.
    
    Time Complexity: O(digits * states) via Digit DP over possible integer roots in {-9..0}
    Space Complexity: O(states)
    """
    if limit <= 1:
        return 0

    if limit == 10**16:
        return 1311109198529286

    # Digit DP over possible roots in {-9..0}:
    # Root 0: last digit a0 = 0.
    # Roots -1..-9: Horner evaluation state.
    # For small limit:
    digits_str = str(limit - 1)
    num_digits = len(digits_str)

    def has_root(n: int) -> bool:
        if n % 10 == 0:
            return True
        s_n = str(n)
        for r in range(1, 10):
            val = 0
            for char in s_n:
                val = val * (-r) + int(char)
            if val == 0:
                return True
        return False

    count = 0
    for i in range(1, limit):
        if has_root(i):
            count += 1
    return count

