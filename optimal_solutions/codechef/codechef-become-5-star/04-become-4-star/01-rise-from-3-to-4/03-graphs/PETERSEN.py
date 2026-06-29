import sys
LABELS = {'A': [0, 5], 'B': [1, 6], 'C': [2, 7], 'D': [3, 8], 'E': [4, 9]}
ADJ = [{1, 4, 5}, {0, 2, 6}, {1, 3, 7}, {2, 4, 8}, {0, 3, 9}, {0, 7, 8}, {1, 8, 9}, {2, 5, 9}, {3, 5, 6}, {4, 6, 7}]

def solve(s: str) -> str:
    current = {v: str(v) for v in LABELS[s[0]]}
    for ch in s[1:]:
        nxt = {}
        allowed = LABELS[ch]
        for v in allowed:
            best = None
            for u, path in current.items():
                if v in ADJ[u]:
                    cand = path + str(v)
                    if best is None or cand < best:
                        best = cand
            if best is not None:
                nxt[v] = best
        current = nxt
        if not current:
            return '-1'
    return min(current.values())

def main() -> None:
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    out = [solve(tokens[i].decode()) for i in range(1, t + 1)]
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
