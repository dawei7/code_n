# cook your dish here


def solve():
    def sumInteger(N):
        return N*(N+1)//2

    def antiSumInt(X):
        return (-1+(1+8*X)**0.5)/2

    for T in range(int(input())):

        N,S = map(int,input().strip().split())

        idealSum = sumInteger(N)

        if S == idealSum:
            print(0)

        else:
            possibleMax = int(antiSumInt(S))
            left = N - possibleMax
            realMax = int(antiSumInt(S-left))

            print(N-realMax)


if __name__ == "__main__":
    solve()
