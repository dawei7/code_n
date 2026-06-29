


def solve():
    n=int(input())
    for i in range(n):
        a=list(input().split())
        x=list(input().split())
        for i in (a):
            if i in x:
                print(i)
                break


if __name__ == "__main__":
    solve()
