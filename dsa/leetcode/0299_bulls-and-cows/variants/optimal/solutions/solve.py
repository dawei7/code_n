"""Linear digit-frequency solution for LeetCode 299: Bulls and Cows."""


def solve(secret: str, guess: str) -> str:
    bulls = 0
    secret_counts = [0] * 10
    guess_counts = [0] * 10
    for secret_digit, guess_digit in zip(secret, guess):
        if secret_digit == guess_digit:
            bulls += 1
        else:
            secret_counts[ord(secret_digit) - ord("0")] += 1
            guess_counts[ord(guess_digit) - ord("0")] += 1
    cows = sum(min(left, right) for left, right in zip(secret_counts, guess_counts))
    return f"{bulls}A{cows}B"
