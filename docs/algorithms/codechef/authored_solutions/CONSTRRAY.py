import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    for n in data[1:1 + t]:
        if n == 1:
            out.append("0")
        elif n % 2:
            out.append("-1")
        else:
            arr = [0] * n
            prev = 0
            for i in range(n // 2):
                want = 1 if i % 2 == 0 else -1
                arr[i] = want - prev
                prev = want
            out.append(" ".join(map(str, arr)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
