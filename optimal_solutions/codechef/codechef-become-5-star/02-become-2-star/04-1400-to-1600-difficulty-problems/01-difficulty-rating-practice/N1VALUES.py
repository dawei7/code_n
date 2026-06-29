


def solve():
    for _ in range(int(input())):
        n = int(input())
        print(1, end=" ")
        for i in range(n):
            print(2**i, end=" ")
        print()


if __name__ == "__main__":
    solve()
