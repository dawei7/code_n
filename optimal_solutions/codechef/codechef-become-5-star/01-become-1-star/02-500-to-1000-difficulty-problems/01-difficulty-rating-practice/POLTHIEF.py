# cook your dish here


def solve():
    for _ in range(int(input())):
        X,Y=map(int,input().split(' '))

        print(abs(X-Y))


if __name__ == "__main__":
    solve()
