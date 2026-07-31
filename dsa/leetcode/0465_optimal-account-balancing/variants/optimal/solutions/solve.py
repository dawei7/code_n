"""Pruned net-balance backtracking for LeetCode 465."""

from collections import defaultdict


def solve(transactions: list[list[int]]) -> int:
    net = defaultdict(int)
    for payer, recipient, amount in transactions:
        net[payer] -= amount
        net[recipient] += amount
    balances = [balance for balance in net.values() if balance]

    def settle(start: int) -> int:
        while start < len(balances) and balances[start] == 0:
            start += 1
        if start == len(balances):
            return 0

        best = len(balances)
        tried = set()
        for partner in range(start + 1, len(balances)):
            if balances[start] * balances[partner] >= 0 or balances[partner] in tried:
                continue
            tried.add(balances[partner])
            original = balances[partner]
            balances[partner] += balances[start]
            best = min(best, 1 + settle(start + 1))
            balances[partner] = original
            if original + balances[start] == 0:
                break
        return best

    return settle(0)
