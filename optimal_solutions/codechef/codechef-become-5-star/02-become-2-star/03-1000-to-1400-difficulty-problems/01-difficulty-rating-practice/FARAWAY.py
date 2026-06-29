


def solve():
    t = int(input())
    for i in range(0,t):
        N,M = map(int,input().split())
        A = list(map(int,input().split()))
        te = 0
        for j in range(N):
            temp = abs(A[j]-1)
            tem = abs(A[j]-M)
            te += max(temp,tem)
        print(te)


if __name__ == "__main__":
    solve()
