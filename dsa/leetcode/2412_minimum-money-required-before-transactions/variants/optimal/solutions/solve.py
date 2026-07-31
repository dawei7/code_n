def solve(transactions: list[list[int]]) -> int:
    unavoidable_loss = sum(max(0, cost - cashback) for cost, cashback in transactions)
    final_bottleneck = max(min(cost, cashback) for cost, cashback in transactions)
    return unavoidable_loss + final_bottleneck
