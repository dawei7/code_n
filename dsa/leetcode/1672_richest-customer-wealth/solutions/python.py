def solve(accounts: list[list[int]]) -> int:
    richest = 0
    for customer in accounts:
        wealth = 0
        for balance in customer:
            wealth += balance
        richest = max(richest, wealth)
    return richest
