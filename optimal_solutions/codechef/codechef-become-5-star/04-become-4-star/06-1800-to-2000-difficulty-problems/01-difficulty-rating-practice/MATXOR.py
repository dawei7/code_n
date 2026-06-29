# cook your dish here


def solve():
    T = int(input())

    for tc in range (T):
        N,M,K = map(int,input().split())
        A = K+2
        if (N == 1 and M == 1):
            print(A)
        else:
            C = 1 # number of times a integer is occuring in matrix. If c is odd net xor would be equal to the element. If c is even net xor would be 0 in binary form.
            A = 0
            # setting row to be >= column for my advantage
            if (M>N):
                temp = M
                M = N
                N = temp
            for i in range(K+2,M+N+K+1):
                if (C%2==1):
                    A ^= i
                if (i <= K+M):
                    C += 1
                elif (i > K+N):
                    C -= 1
            print(A)


if __name__ == "__main__":
    solve()
