# cook your dish here


def solve():
    for i in range(int(input())):
        n=int(input())
        p=1
        for i in range(1,n+1):
            p=p*i
        print(p)


if __name__ == "__main__":
    solve()
