import sys


MAX_EFFECTIVE_K = 70


def precompute(max_n: int, max_k: int) -> list[list[float]]:
    layers = [[float(i) for i in range(max_n + 1)]]
    for _ in range(max_k):
        prev = layers[-1]
        curr = [0.0] * (max_n + 1)
        prefix = 0.0
        for n in range(1, max_n + 1):
            prefix += prev[n - 1]
            curr[n] = prefix / n
        layers.append(curr)
    return layers


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    queries = [(data[i], data[i + 1]) for i in range(1, 2 * t + 1, 2)]
    max_n = max((n for n, _ in queries), default=0)
    max_k = min(max((k for _, k in queries), default=0), MAX_EFFECTIVE_K)
    layers = precompute(max_n, max_k)
    out = []
    for n, k in queries:
        if k > MAX_EFFECTIVE_K:
            out.append("0.0000000000")
        else:
            out.append(f"{layers[k][n]:.10f}")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
