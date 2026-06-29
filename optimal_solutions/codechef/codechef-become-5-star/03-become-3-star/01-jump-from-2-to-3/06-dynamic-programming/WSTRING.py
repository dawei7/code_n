import sys

def longest_w_string(text: str) -> int:
    n = len(text)
    hashes = [i for i, ch in enumerate(text) if ch == '#']
    if len(hashes) < 3:
        return 0
    prefix_best = [0] * n
    counts = [0] * 26
    best = 0
    for i, ch in enumerate(text):
        prefix_best[i] = best
        if ch != '#':
            idx = ord(ch) - 97
            counts[idx] += 1
            if counts[idx] > best:
                best = counts[idx]
    suffix_best = [0] * n
    counts = [0] * 26
    best = 0
    for i in range(n - 1, -1, -1):
        suffix_best[i] = best
        ch = text[i]
        if ch != '#':
            idx = ord(ch) - 97
            counts[idx] += 1
            if counts[idx] > best:
                best = counts[idx]
    block_best: dict[tuple[int, int], int] = {}
    for left, right in zip(hashes, hashes[1:]):
        counts = [0] * 26
        best = 0
        for i in range(left + 1, right):
            idx = ord(text[i]) - 97
            counts[idx] += 1
            if counts[idx] > best:
                best = counts[idx]
        block_best[left, right] = best
    answer = 0
    for i in range(len(hashes) - 2):
        p1, p2, p3 = (hashes[i], hashes[i + 1], hashes[i + 2])
        parts = (prefix_best[p1], block_best[p1, p2], block_best[p2, p3], suffix_best[p3])
        if all(parts):
            answer = max(answer, sum(parts) + 3)
    return answer

def solve() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    t = int(tokens[0])
    out = [str(longest_w_string(tokens[i].decode())) for i in range(1, t + 1)]
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
