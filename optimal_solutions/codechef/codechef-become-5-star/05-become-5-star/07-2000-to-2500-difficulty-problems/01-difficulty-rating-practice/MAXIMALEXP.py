


def solve():
    t = int(input())
    for _ in range(t):
        n,k = list(map(int,input().split()))
        K = min(n,k-1)
        if K==0:
            print(K)
            continue
        a = (n-K)%k
        b = (K // 2) + (K % 2)
        print(b+a//2)


if __name__ == "__main__":
    solve()
