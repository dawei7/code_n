# cook your dish here


def solve():
    for i in range(int(input())):
        X= set(map(int,input().split()))
        print(len(X)-2)


if __name__ == "__main__":
    solve()
