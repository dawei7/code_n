


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        a.sort()

        if a == b:
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    solve()
