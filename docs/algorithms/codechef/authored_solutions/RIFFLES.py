import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, k = data[idx:idx + 2]
        idx += 2
        perm = list(range(n))
        order = list(range(0, n, 2)) + list(range(1, n, 2))
        visited = [False] * n
        ans = [0] * n
        for i in range(n):
            if visited[i]:
                continue
            cyc = []
            cur = i
            while not visited[cur]:
                visited[cur] = True
                cyc.append(cur)
                cur = order[cur]
            shift = k % len(cyc)
            for pos, old_pos in enumerate(cyc):
                ans[cyc[pos]] = perm[cyc[(pos + shift) % len(cyc)]] + 1
        out.append(" ".join(map(str, ans)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
