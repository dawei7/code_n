


def solve():
    for _ in range(int(input())):
        a,b,c,d=map(int,input().split(" "))
        print(a+((d*b)-(c*d)))


if __name__ == "__main__":
    solve()
