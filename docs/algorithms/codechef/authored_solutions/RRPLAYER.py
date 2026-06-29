import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    max_n = max(data[1:], default=0)
    harmonic = [0.0] * (max_n + 1)
    for i in range(1, max_n + 1):
        harmonic[i] = harmonic[i - 1] + 1.0 / i
    out = [f"{n * harmonic[n]:.10f}" for n in data[1:]]
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
