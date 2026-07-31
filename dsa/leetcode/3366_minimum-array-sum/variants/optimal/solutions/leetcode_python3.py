class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        infinity = 10**18
        dp = [[infinity] * (op2 + 1) for _ in range(op1 + 1)]
        dp[0][0] = 0

        for value in nums:
            half = (value + 1) // 2
            options = [(value, 0, 0), (half, 1, 0)]
            if value >= k:
                options.append((value - k, 0, 1))
                options.append(((value - k + 1) // 2, 1, 1))
            if half >= k:
                options.append((half - k, 1, 1))

            next_dp = [[infinity] * (op2 + 1) for _ in range(op1 + 1)]
            for used1 in range(op1 + 1):
                for used2 in range(op2 + 1):
                    current = dp[used1][used2]
                    if current == infinity:
                        continue
                    for transformed, add1, add2 in options:
                        next1 = used1 + add1
                        next2 = used2 + add2
                        if next1 <= op1 and next2 <= op2:
                            next_dp[next1][next2] = min(
                                next_dp[next1][next2], current + transformed
                            )
            dp = next_dp

        return min(map(min, dp))
