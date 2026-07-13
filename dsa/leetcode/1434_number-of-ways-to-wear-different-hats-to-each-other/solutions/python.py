from collections import defaultdict


def solve(hats):
    mod = 1_000_000_007
    people = len(hats)
    if people == 0:
        return 1
    by_hat = defaultdict(list)
    for person, choices in enumerate(hats):
        if not isinstance(choices, list):
            choices = [choices]
        for hat in choices:
            by_hat[int(hat)].append(person)
    if people > len(by_hat):
        return 0
    dp = {0: 1}
    full = (1 << people) - 1
    for hat in sorted(by_hat):
        next_dp = dict(dp)
        for mask, count in dp.items():
            for person in by_hat[hat]:
                bit = 1 << person
                if not mask & bit:
                    next_dp[mask | bit] = (next_dp.get(mask | bit, 0) + count) % mod
        dp = next_dp
    return dp.get(full, 0)
