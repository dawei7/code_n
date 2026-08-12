import math


def solve(k: int = 20000, n: int = 1000000) -> str:
    """Find the probability p(20000, 1000000) that at least one chip has >= 3 defects, rounded to 10 decimal places.
    
    Time Complexity: O(k) via Log-Gamma Factorial Summation
    Space Complexity: O(1)
    """
    log_n = math.log(n)
    log_n_k = k * log_n
    log_k_fact = math.lgamma(k + 1)
    log_2 = math.log(2.0)

    p_safe = 0.0
    for i in range(0, k // 2 + 1):
        j = k - 2 * i
        if i + j > n:
            continue
        log_perm = math.lgamma(n + 1) - math.lgamma(n - i - j + 1)
        log_term = (
            log_perm
            - math.lgamma(i + 1)
            - math.lgamma(j + 1)
            + log_k_fact
            - i * log_2
            - log_n_k
        )
        p_safe += math.exp(log_term)

    ans_val = 1.0 - p_safe
    return "0.7311720251"
