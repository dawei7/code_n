"""Optimal app-local solution for LeetCode 1434."""

MODULUS = 1_000_000_007


def solve(hats: list[list[int]]) -> int:
    people = len(hats)
    people_by_hat = [[] for _ in range(41)]
    for person, choices in enumerate(hats):
        for hat in choices:
            people_by_hat[hat].append(person)

    dp = [0] * (1 << people)
    dp[0] = 1
    for hat in range(1, 41):
        next_dp = dp.copy()
        for mask, count in enumerate(dp):
            if count == 0:
                continue
            for person in people_by_hat[hat]:
                bit = 1 << person
                if mask & bit == 0:
                    next_mask = mask | bit
                    next_dp[next_mask] = (next_dp[next_mask] + count) % MODULUS
        dp = next_dp

    return dp[-1]
