import sys


MOD = 7_051_954


def count_sequences(n: int, length: int, start: int, finish: int, mcq: str) -> int:
    next_plus = [-1] * n
    next_minus = [-1] * n
    plus_count = [0] * n
    minus_count = [0] * n

    plus_pos = -1
    minus_pos = -1
    plus_seen = 0
    minus_seen = 0
    for i in range(n - 1, -1, -1):
        if mcq[i] == "+":
            plus_pos = i
            plus_seen += 1
        else:
            minus_pos = i
            minus_seen += 1
        next_plus[i] = plus_pos
        next_minus[i] = minus_pos
        plus_count[i] = plus_seen
        minus_count[i] = minus_seen

    farthest_right = min(start + plus_count[0], length)
    farthest_left = max(start - minus_count[0], 0)
    if finish < farthest_left or finish > farthest_right:
        return 0

    width = farthest_right - farthest_left + 1
    dp = [[0] * (n + 1) for _ in range(width)]
    dp[finish - farthest_left][n] = 1

    for command_start in range(n - 1, -1, -1):
        np = next_plus[command_start]
        nm = next_minus[command_start]
        for position in range(farthest_left, farthest_right + 1):
            cur = position - farthest_left
            value = 0
            if np != -1 and position + 1 <= farthest_right:
                value += dp[cur + 1][np + 1]
            if nm != -1 and position - 1 >= farthest_left:
                value += dp[cur - 1][nm + 1]
            if position == finish:
                value += 1
            dp[cur][command_start] = value % MOD

    return dp[start - farthest_left][0]


def main() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    t = int(tokens[0])
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = int(tokens[idx])
        length = int(tokens[idx + 1])
        start = int(tokens[idx + 2])
        finish = int(tokens[idx + 3])
        mcq = tokens[idx + 4].decode()
        idx += 5
        out.append(str(count_sequences(n, length, start, finish, mcq)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
