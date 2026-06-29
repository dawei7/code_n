# cook your dish here


def solve():
    for i in range(int(input())):
        S=list(map(int,input().split()))
        S.sort()
        print(S[1])


if __name__ == "__main__":
    solve()
