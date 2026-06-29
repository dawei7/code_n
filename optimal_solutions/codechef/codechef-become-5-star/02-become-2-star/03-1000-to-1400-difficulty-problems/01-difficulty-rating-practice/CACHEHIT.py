# cook your dish here


def solve():
    for i in range(int(input())):
        N,B,M = map(int,input().split())
        x = list(map(int,input().split()))
        a = 1
        for i in range(M-1):
            if x[i] // B != x[i+1] // B:
                a += 1
        print(a)


if __name__ == "__main__":
    solve()
