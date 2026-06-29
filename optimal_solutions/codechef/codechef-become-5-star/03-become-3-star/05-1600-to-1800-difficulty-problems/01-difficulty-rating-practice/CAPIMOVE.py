import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    answers = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        pop = data[idx:idx + n]
        idx += n
        adj = [set() for _ in range(n)]
        for _ in range(n - 1):
            u = data[idx] - 1
            v = data[idx + 1] - 1
            idx += 2
            adj[u].add(v)
            adj[v].add(u)
        order = sorted(range(n), key=lambda i: pop[i], reverse=True)
        res = []
        for v in range(n):
            chosen = 0
            blocked = adj[v]
            for candidate in order:
                if candidate != v and candidate not in blocked:
                    chosen = candidate + 1
                    break
            res.append(str(chosen))
        answers.append(' '.join(res))
    sys.stdout.write('\n'.join(answers))


if __name__ == "__main__":
    solve()
