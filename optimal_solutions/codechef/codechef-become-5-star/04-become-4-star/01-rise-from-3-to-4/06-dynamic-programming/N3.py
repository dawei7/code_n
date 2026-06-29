import sys

def prefix_function(text: str) -> list[int]:
    pi = [0] * len(text)
    for i in range(1, len(text)):
        j = pi[i - 1]
        while j and text[i] != text[j]:
            j = pi[j - 1]
        if text[i] == text[j]:
            j += 1
        pi[i] = j
    return pi

def overlap(a: str, b: str) -> int:
    if len(a) == 1:
        return 0
    return prefix_function(b + '{' + a[1:])[-1]

def solve_case(strings: list[str], k: int) -> list[str]:
    n = len(strings)
    length = len(strings[0])
    overlaps = [[0] * n for _ in range(n)]
    for i, left in enumerate(strings):
        for j, right in enumerate(strings):
            overlaps[i][j] = overlap(left, right)
    inf = 10 ** 12
    dp = [[length] * n]
    parent = [[-1] * n for _ in range(k)]
    for used in range(1, k):
        prev = dp[-1]
        cur = [inf] * n
        for last in range(n):
            best_value = inf
            best_prev = 0
            for before in range(n):
                value = prev[before] + length - overlaps[before][last]
                if value < best_value:
                    best_value = value
                    best_prev = before
            cur[last] = best_value
            parent[used][last] = best_prev
        dp.append(cur)
    best = min(range(n), key=lambda idx: dp[k - 1][idx])
    order = [0] * k
    for pos in range(k - 1, -1, -1):
        order[pos] = best
        best = parent[pos][best]
    pieces = [strings[order[0]]]
    positions: list[tuple[int, int]] = []
    at = 0
    for pos in range(k - 1):
        current = order[pos]
        nxt = order[pos + 1]
        positions.append((current, at))
        at += length - overlaps[current][nxt]
        pieces.append(strings[nxt][overlaps[current][nxt]:])
    positions.append((order[-1], at))
    constructed = ''.join(pieces)
    lines = [str(len(constructed)), constructed]
    lines.extend((f'{idx} {position}' for idx, position in positions))
    return lines

def solve() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    t = int(tokens[0])
    idx = 1
    chunks: list[str] = []
    for case_no in range(t):
        n = int(tokens[idx])
        _length = int(tokens[idx + 1])
        k = int(tokens[idx + 2])
        idx += 3
        strings = [tokens[idx + i].decode() for i in range(n)]
        idx += n
        chunks.append('\n'.join(solve_case(strings, k)))
    sys.stdout.write('\n\n'.join(chunks))


if __name__ == "__main__":
    solve()
