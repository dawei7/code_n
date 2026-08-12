A_STR = '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
B_STR = '8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196'


def solve(max_n: int = 17) -> int:
    """Find sum_{n=0..17} 10^n * D_{A,B}((127 + 19n) * 7^n).
    
    Time Complexity: O(max_n * log_phi(target_idx))
    Space Complexity: O(log_phi(target_idx))
    """
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
        else:
            return int(B_STR[curr_n - 1])

    ans_sum = 0
    for n in range(max_n + 1):
        idx = (127 + 19 * n) * (7**n)
        d = get_digit(idx)
        ans_sum += (10**n) * d

    return ans_sum
