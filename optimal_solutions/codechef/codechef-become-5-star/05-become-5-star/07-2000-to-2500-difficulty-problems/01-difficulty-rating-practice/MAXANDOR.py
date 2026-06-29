


def solve():
    t = int(input())
    for _ in range(t):
        a,b,c = list(map(int,input().split()))
        n = pow(2,c) - 1
        N = len(bin(n)[2:])
        aa = bin(a)[2:]
        bb = bin(b)[2:]
        A = '0'*(N-len(aa)) + aa
        B = '0'*(N-len(bb)) + bb
        ans = 1
        for i in range(len(A)):
            if A[i]!=B[i]:
                ans *= 2
        print(ans)


if __name__ == "__main__":
    solve()
