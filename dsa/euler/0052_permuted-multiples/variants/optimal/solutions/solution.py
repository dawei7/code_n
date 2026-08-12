def solve() -> int:
    """Find smallest positive integer x such that x, 2x, 3x, 4x, 5x, 6x contain the same digits.
    
    Time Complexity: O(x * d log d)
    Space Complexity: O(d)
    """
    x = 1
    while True:
        s_x = sorted(str(x))
        if (
            sorted(str(2 * x)) == s_x
            and sorted(str(3 * x)) == s_x
            and sorted(str(4 * x)) == s_x
            and sorted(str(5 * x)) == s_x
            and sorted(str(6 * x)) == s_x
        ):
            return x
        x += 1
