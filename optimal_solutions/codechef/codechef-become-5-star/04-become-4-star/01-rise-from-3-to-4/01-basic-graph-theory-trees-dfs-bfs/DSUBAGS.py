import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, q = (data[0], data[1])
    parent = list(range(n + 1))
    size = [1] * (n + 1)
    components = n

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    out = []
    idx = 2
    for _ in range(q):
        typ = data[idx]
        idx += 1
        if typ == 3:
            out.append(str(components))
            continue
        a, b = (data[idx], data[idx + 1])
        idx += 2
        ra, rb = (find(a), find(b))
        if typ == 1:
            if ra != rb:
                if size[ra] < size[rb]:
                    ra, rb = (rb, ra)
                parent[rb] = ra
                size[ra] += size[rb]
                components -= 1
        else:
            out.append('YES' if ra == rb else 'NO')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
