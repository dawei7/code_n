import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        min_a = 10**18
        min_b = 10**18
        for _ in range(n):
            s = data[idx]
            idx += 1
            count_a = s.count(b"a")
            min_a = min(min_a, count_a)
            min_b = min(min_b, len(s) - count_a)
        out.append(str(min(min_a, min_b)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
