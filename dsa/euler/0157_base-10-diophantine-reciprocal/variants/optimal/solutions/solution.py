import math


def count_divisors(n: int) -> int:
    """Find number of positive divisors d(n)."""
    cnt = 1
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            exp = 0
            while temp % d == 0:
                exp += 1
                temp //= d
            cnt *= (exp + 1)
        d += 1
    if temp > 1:
        cnt *= 2
    return cnt


def solve(max_n: int = 9) -> int:
    """Find total number of solutions to 1/a + 1/b = p/10^n for 1 <= n <= max_n.
    
    Time Complexity: O(max_n * Divs(10^n)^2)
    Space Complexity: O(Divs(10^n))
    """
    total_solutions = 0

    for n in range(1, max_n + 1):
        pow10 = 10**n
        divs = [2**a * 5**b for a in range(n + 1) for b in range(n + 1)]
        divs.sort()

        n_sols = 0
        for i in range(len(divs)):
            A = divs[i]
            for j in range(i, len(divs)):
                B = divs[j]
                if math.gcd(A, B) == 1:
                    K = (pow10 * (A + B)) // (A * B)
                    n_sols += count_divisors(K)

        total_solutions += n_sols

    return total_solutions
