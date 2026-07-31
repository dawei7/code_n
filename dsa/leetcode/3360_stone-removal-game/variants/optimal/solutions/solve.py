def solve(n: int) -> bool:
    required = 10
    alice_wins = False

    while n >= required:
        n -= required
        required -= 1
        alice_wins = not alice_wins

    return alice_wins
