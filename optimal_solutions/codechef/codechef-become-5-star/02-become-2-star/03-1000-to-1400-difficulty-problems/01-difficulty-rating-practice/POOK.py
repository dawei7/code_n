# cook your dish here


def solve():
    for _ in range(int(input())):
        n = int(input())
        print(n if n > 3 else n-1 if n>1 else 1)


if __name__ == "__main__":
    solve()
