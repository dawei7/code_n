def solve(s1: str, s2: str) -> bool:
    balance = [0] * 52

    for index, (left, right) in enumerate(zip(s1, s2)):
        offset = 26 * (index & 1)
        balance[offset + ord(left) - ord("a")] += 1
        balance[offset + ord(right) - ord("a")] -= 1

    return not any(balance)
