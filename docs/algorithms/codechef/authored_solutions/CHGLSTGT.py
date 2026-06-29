import sys


def minimum_palindrome_parts(text: str) -> int:
    n = len(text)
    dp = list(range(n + 1))

    for center in range(n):
        left = right = center
        while left >= 0 and right < n and text[left] == text[right]:
            value = dp[left] + 1
            if value < dp[right + 1]:
                dp[right + 1] = value
            left -= 1
            right += 1

        left, right = center, center + 1
        while left >= 0 and right < n and text[left] == text[right]:
            value = dp[left] + 1
            if value < dp[right + 1]:
                dp[right + 1] = value
            left -= 1
            right += 1

    return dp[n]


def main() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    t = int(tokens[0])
    idx = 1
    out: list[str] = []
    for _ in range(t):
        _n = int(tokens[idx])
        text = tokens[idx + 1].decode()
        idx += 2
        out.append(str(minimum_palindrome_parts(text)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
