# cook your dish here


def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        A.sort()
        if A[1] - A[0] != 1:
            print(A[0])
        elif A[-1] - A[-2] != 1:
            print(A[-1])
        else:
            for i in range(1, N):
                if A[i] == A[i-1]:
                    print(A[i-1])


if __name__ == "__main__":
    solve()
