from heapq import heappop, heappush


def solve(transactions: list[int]) -> int:
    selected: list[int] = []
    balance = 0

    for amount in transactions:
        heappush(selected, amount)
        balance += amount

        if balance < 0:
            balance -= heappop(selected)

    return len(selected)
