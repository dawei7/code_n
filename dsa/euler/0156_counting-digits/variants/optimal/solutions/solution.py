def f(n: int, d: int) -> int:
    """Find total occurrences of digit d in numbers from 0 to n."""
    if n <= 0:
        return 0
    s = str(n)
    total = 0
    L = len(s)
    for i, c in enumerate(s):
        digit = int(c)
        pow10 = 10 ** (L - 1 - i)
        prefix = int(s[:i]) if i > 0 else 0
        total += prefix * pow10
        if digit > d:
            total += pow10
        elif digit == d:
            suffix = int(s[i + 1:]) if i + 1 < L else 0
            total += suffix + 1
    return total


def search_solutions(d: int, low: int, high: int) -> int:
    """Divide-and-conquer search for all n in [low, high] satisfying f(n, d) == n."""
    f_low = f(low, d)
    f_high = f(high, d)

    # Monotonic interval bounds check (Pruning)
    if f_low > high or f_high < low:
        return 0

    if low == high:
        if f_low == low and low > 0:
            return low
        return 0

    mid = (low + high) // 2
    return search_solutions(d, low, mid) + search_solutions(d, mid + 1, high)


def solve(max_val: int = 10**11) -> int:
    """Find sum s(d) for all 1 <= d <= 9 of n > 0 satisfying f(n, d) == n.
    
    Time Complexity: O(Digits * log(MaxVal) * PruningFactor)
    Space Complexity: O(log(MaxVal))
    """
    return sum(search_solutions(d, 0, max_val) for d in range(1, 10))
