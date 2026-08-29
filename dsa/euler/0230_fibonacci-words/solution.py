def solve(max_n: int = 17) -> int:
    """Find sum_{n=0..17} 10^n * D_{A,B}((127 + 19n) * 7^n) for Fibonacci words over pi and e digits.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Fibonacci Word Definition:
       Let string A be the first 100 digits of pi (after the decimal point), and string B be the
       first 100 digits of e (after the decimal point).
       The sequence of Fibonacci words is defined by:
           W_1 = A
           W_2 = B
           W_k = W_{k-2} + W_{k-1}  for k >= 3.
       Length of W_k satisfies:
           |W_1| = 100, |W_2| = 100, |W_k| = |W_{k-2}| + |W_{k-1}|.

    2. Recursive Digit Navigation / Logarithmic Search:
       To find the character at index p in W_k (1-indexed):
       - If p <= |W_{k-2}|: the character is at index p in W_{k-2}.
       - If p > |W_{k-2}|: the character is at index (p - |W_{k-2}|) in W_{k-1}.
       By descending until k in {1, 2}, we retrieve the character directly from string A or B
       in O(log_phi(p)) time.

    3. Evaluation of Target Indices:
       For n in 0..17, target indices are p_n = (127 + 19n) * 7^n.
       Total value is sum_{n=0}^{17} 10^n * digit(p_n).

    Complexity:
    -----------
    - Time Complexity: O(max_n * log_phi(p_max)) operations (~0.0001s for max_n = 17).
    - Space Complexity: O(log_phi(p_max)) length table (< 1 KB).
    """
    A_STR = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    B_STR = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"

    L0 = len(A_STR)
    L = [0, L0, L0]
    while L[-1] < 10**25:
        L.append(L[-1] + L[-2])

    def get_digit(n: int) -> int:
        k = 1
        while L[k] < n:
            k += 1

        curr_n = n
        curr_k = k
        while curr_k > 2:
            l_prev = L[curr_k - 2]
            if curr_n <= l_prev:
                curr_k -= 2
            else:
                curr_n -= l_prev
                curr_k -= 1

        if curr_k == 1:
            return int(A_STR[curr_n - 1])
        return int(B_STR[curr_n - 1])

    ans_sum = 0
    for n in range(max_n + 1):
        idx = (127 + 19 * n) * (7**n)
        d = get_digit(idx)
        ans_sum += (10**n) * d

    return ans_sum


if __name__ == "__main__":
    print(solve())
