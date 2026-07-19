def solve(s: str) -> int:
    balance = 0
    minimum_balance = 0

    for bracket in s:
        if bracket == "[":
            balance += 1
        else:
            balance -= 1
        minimum_balance = min(minimum_balance, balance)

    deficit = -minimum_balance
    return (deficit + 1) // 2
