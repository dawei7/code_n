class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        modulo = 1_000_000_007
        maximum = n * (n - 1) // 2
        if k > maximum:
            return 0
        k = min(k, maximum - k)

        previous = [0] * (k + 1)
        previous[0] = 1
        for length in range(1, n + 1):
            current = [0] * (k + 1)
            window = 0
            for inversions in range(k + 1):
                window += previous[inversions]
                if inversions >= length:
                    window -= previous[inversions - length]
                current[inversions] = window % modulo
            previous = current
        return previous[k]
