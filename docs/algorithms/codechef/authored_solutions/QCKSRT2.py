import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    pairs = data[1:1 + 2 * n]
    seen = set()
    ans = []
    for i in range(n):
        first = pairs[2 * i]
        if first not in seen:
            seen.add(first)
            ans.append(i)
    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
