import sys


def compressed(text: bytes) -> list[int]:
    result: list[int] = []
    prev = None
    for ch in text:
        if ch != prev:
            result.append(ch)
            prev = ch
    return result


def minimum_blocks(a: bytes, b: bytes) -> int:
    left = compressed(a)
    right = compressed(b)
    if len(left) < len(right):
        left, right = right, left

    dp = [0] * (len(right) + 1)
    for ch in left:
        prev = 0
        for j, other in enumerate(right, 1):
            old = dp[j]
            if ch == other:
                dp[j] = prev + 1
            elif dp[j - 1] > dp[j]:
                dp[j] = dp[j - 1]
            prev = old
    return len(left) + len(right) - dp[-1]


def main() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    t = int(tokens[0])
    idx = 1
    out: list[str] = []
    for _ in range(t):
        _n = int(tokens[idx])
        _m = int(tokens[idx + 1])
        a = tokens[idx + 2]
        b = tokens[idx + 3]
        idx += 4
        out.append(str(minimum_blocks(a, b)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
