import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    arr = data[1:]
    if n > 130:
        print("Yes")
        return

    seen = {}
    for i in range(n):
        for j in range(i + 1, n):
            value = arr[i] ^ arr[j]
            for a, b in seen.get(value, []):
                if a != i and a != j and b != i and b != j:
                    print("Yes")
                    return
            seen.setdefault(value, []).append((i, j))
    print("No")


if __name__ == "__main__":
    main()
