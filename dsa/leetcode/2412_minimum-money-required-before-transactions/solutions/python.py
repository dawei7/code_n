from typing import List

def solve(transactions: List[List[int]]) -> int:
    """
    Calculates the minimum initial money required to complete all transactions.
    """
    total_loss = sum(max(0, cost - cashback) for cost, cashback in transactions)
    answer = 0

    for cost, cashback in transactions:
        if cost > cashback:
            answer = max(answer, total_loss + cashback)
        else:
            answer = max(answer, total_loss + cost)

    return answer
