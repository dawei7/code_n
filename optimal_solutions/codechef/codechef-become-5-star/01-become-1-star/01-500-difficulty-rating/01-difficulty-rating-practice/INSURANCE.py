


def solve():
    for _ in range(int(input())):
        x,y=map(int,input().split(" "))
        if y<x:
            print(y)
        else:
            print(x)


if __name__ == "__main__":
    solve()
