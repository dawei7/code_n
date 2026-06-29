


def solve():
    for _ in range(int(input())):
        n = int(input())
        if n & (n + 1) == 0:
            print(n + 1)
        else:
            mask = n.bit_length()
            print(1 << (mask - 1))


if __name__ == "__main__":
    solve()
