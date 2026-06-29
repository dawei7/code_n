import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, m = data[idx], data[idx + 1]
        idx += 2
        degree = [0] * (n + 1)
        first_edge = (1, 2)
        for e in range(m):
            u, v = data[idx], data[idx + 1]
            idx += 2
            if e == 0:
                first_edge = (u, v)
            degree[u] += 1
            degree[v] += 1
        if m % 2 == 0:
            out.append("1")
            out.append(" ".join(["1"] * n))
        else:
            odd_vertex = next((i for i in range(1, n + 1) if degree[i] % 2 == 1), -1)
            if odd_vertex != -1:
                labels = ["1"] * n
                labels[odd_vertex - 1] = "2"
                out.append("2")
                out.append(" ".join(labels))
            else:
                labels = ["1"] * n
                labels[first_edge[0] - 1] = "2"
                labels[first_edge[1] - 1] = "3"
                out.append("3")
                out.append(" ".join(labels))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
