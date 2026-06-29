# cook your dish here


def solve():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        for i in range(1, k + 1):
            print(i, end=" ")
        i = k + 2
        while i <= n:
            print(i, end=" ")
            i += 2
        j = k + 1
        while j <= n:
            print(j, end=" ")
            j += 2
        print()


if __name__ == "__main__":
    solve()
