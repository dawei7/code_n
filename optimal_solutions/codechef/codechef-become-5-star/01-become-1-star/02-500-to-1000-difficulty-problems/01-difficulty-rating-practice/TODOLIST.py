# cook your dish here


def solve():
    T = int(input())
    for i in range(T):
        N = int(input())
        D = list(map(int,input().split()))
        count = 0
        for i in range(N):
            if D[i]>=1000:
                count = count+1
                continue
        print(count)


if __name__ == "__main__":
    solve()
