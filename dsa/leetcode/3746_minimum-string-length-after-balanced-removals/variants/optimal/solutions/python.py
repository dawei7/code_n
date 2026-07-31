def solve(s: str) -> int:
    balance = 0
    for character in s:
        if character == "a":
            balance += 1
        else:
            balance -= 1
    return abs(balance)
