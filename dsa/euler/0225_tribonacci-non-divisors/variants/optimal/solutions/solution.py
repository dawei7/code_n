def solve(target_index: int = 124) -> int:
    """Find the N-th odd number that does not divide any term of Tribonacci sequence.
    
    Time Complexity: O(N * period_avg)
    Space Complexity: O(1)
    """

    def is_non_divisor(k):
        a, b, c = 1, 1, 1
        while True:
            d = (a + b + c) % k
            if d == 0:
                return False
            a, b, c = b, c, d
            if (a, b, c) == (1, 1, 1):
                return True

    non_divisors = []
    k = 3
    while len(non_divisors) < target_index:
        if is_non_divisor(k):
            non_divisors.append(k)
        k += 2

    return non_divisors[target_index - 1]
