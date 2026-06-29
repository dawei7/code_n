# cook your dish here


def solve():
    for _ in range(int(input())):
        n = int(input())
        summa = n*(n+1)/2
        if summa%2 == 0:
            print(n)
        else:
            print(n-1)


if __name__ == "__main__":
    solve()
