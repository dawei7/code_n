# cook your dish here


def solve():
    mod = 10**9 + 7


    for _ in range(int(input())):
        N, K = list(map(int, input().split()))
        if N == K:
            print(2); continue
        sm = [0]*N
        vals = [0]*N
        for i in range(N):
            if i < K:
                vals[i] = 1
            else:
                vals[i] = (sm[i - K] + 1) % mod
            if i != 0: sm[i] = (sm[i - 1] + vals[i]) % mod
            else: sm[i] = (vals[i]) % mod
        print((sm[-K] + 1) % mod)


if __name__ == "__main__":
    solve()
