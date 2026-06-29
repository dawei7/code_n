


def solve():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        girls = list(map(int, input().split()))
        currentImpressed = sum(girls[:K])
        maxImpressed = currentImpressed
        for i in range(K, N):
            currentImpressed = currentImpressed - girls[i - K] + girls[i]
            maxImpressed = max(maxImpressed, currentImpressed)
        print(maxImpressed)


if __name__ == "__main__":
    solve()
