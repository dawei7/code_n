import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        arr = data[idx:idx + n]
        idx += n
        best = {}
        parent = {}
        pref = 0
        best[0] = (1, 0)
        parent[0] = None
        node_id = 1
        nodes = [(1, 1)]
        for pos, bit in enumerate(arr, 1):
            pref += 1 if bit == 1 else -1
            prev = best.get(pref - 1)
            length = 1
            prev_id = None
            if prev:
                length = prev[0] + 1
                prev_id = prev[1]
            if length > best.get(pref, (0, -1))[0]:
                best[pref] = (length, node_id)
                parent[node_id] = prev_id
                nodes.append((pos + 1, length))
                node_id += 1
        end_id = max((v[1] for v in best.values()), key=lambda i: nodes[i][1])
        seq = []
        cur = end_id
        while cur is not None:
            seq.append(nodes[cur][0])
            cur = parent[cur]
        seq.reverse()
        out.append(str(len(seq)))
        out.append(" ".join(map(str, seq)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
