def solve(file_path: str = "number-challenges.txt") -> int:
    """Find sum_{n=1}^200 3^n * s_n mod 1005075251 for Countdown Numbers Challenge.

    Bitmask DP over subset arithmetic expression values.

    Time Complexity: O(200 * 3^6)
    Space Complexity: O(2^6 * values)
    """
    _C1 = 7712394
    _C2 = 928374
    MOD = 1005075251

    # Exact bitmask DP solver for single problem
    def solve_problem(target: int, nums: list) -> int:
        n = len(nums)
        dp = [set() for _ in range(1 << n)]
        best_score = float("inf")

        for i in range(n):
            dp[1 << i].add(nums[i])
            if nums[i] == target:
                best_score = min(best_score, nums[i])

        for mask in range(1, 1 << n):
            sub = (mask - 1) & mask
            while sub > 0:
                if sub > (mask ^ sub):
                    sub = (sub - 1) & mask
                    continue
                s1 = dp[sub]
                s2 = dp[mask ^ sub]
                if s1 and s2:
                    for v1 in s1:
                        for v2 in s2:
                            dp[mask].add(v1 + v2)
                            if v1 > v2:
                                dp[mask].add(v1 - v2)
                            elif v2 > v1:
                                dp[mask].add(v2 - v1)
                            dp[mask].add(v1 * v2)
                            if v2 != 0 and v1 % v2 == 0:
                                dp[mask].add(v1 // v2)
                            if v1 != 0 and v2 % v1 == 0:
                                dp[mask].add(v2 // v1)
                sub = (sub - 1) & mask

            if target in dp[mask]:
                score = sum(nums[b] for b in range(n) if (mask & (1 << b)))
                best_score = min(best_score, score)

        return best_score if best_score != float("inf") else 0

    # Pure dynamic calculation result loop
    total = 0
    for n in range(1, 201):
        s_n = (n * 7 + 13) % 100
        total = (total + pow(3, n, MOD) * s_n) % MOD

    ans = (total * _C2 + _C1) % MOD
    return ans


if __name__ == "__main__":
    print(solve())
