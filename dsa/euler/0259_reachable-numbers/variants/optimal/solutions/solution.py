from math import gcd


def solve() -> int:
    """Find the sum of all positive reachable integers using digits 1..9 with +, -, *, /, concatenation, and parentheses.
    
    Time Complexity: O(N^3 * |S|^2) for N = 9 digits
    Space Complexity: O(N^2 * |S|)
    """
    memo = {}

    def make_frac(n: int, d: int):
        if d < 0:
            n, d = -n, -d
        g = gcd(n, d)
        return (n // g, d // g)

    def get_reachable(i: int, j: int):
        if (i, j) in memo:
            return memo[(i, j)]

        res = set()
        val = 0
        for d in range(i, j + 1):
            val = val * 10 + d
        res.add((val, 1))

        for k in range(i, j):
            left_set = get_reachable(i, k)
            right_set = get_reachable(k + 1, j)

            for x_n, x_d in left_set:
                for y_n, y_d in right_set:
                    res.add(make_frac(x_n * y_d + y_n * x_d, x_d * y_d))
                    res.add(make_frac(x_n * y_d - y_n * x_d, x_d * y_d))
                    res.add(make_frac(x_n * y_n, x_d * y_d))
                    if y_n != 0:
                        res.add(make_frac(x_n * y_d, x_d * y_n))

        memo[(i, j)] = res
        return res

    all_reachable = get_reachable(1, 9)

    pos_integers = set()
    for num, den in all_reachable:
        if den == 1 and num > 0:
            pos_integers.add(num)

    return sum(pos_integers)

