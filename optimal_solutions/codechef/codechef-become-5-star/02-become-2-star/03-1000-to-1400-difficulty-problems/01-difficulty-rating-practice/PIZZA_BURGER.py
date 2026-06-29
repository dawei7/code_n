


def solve():
    t=int(input())
    for _ in range(t):
        a,b,c=map(int,input().split())
        print("PIZZA" if a>=b else "BURGER" if a>=c else "NOTHING")


if __name__ == "__main__":
    solve()
