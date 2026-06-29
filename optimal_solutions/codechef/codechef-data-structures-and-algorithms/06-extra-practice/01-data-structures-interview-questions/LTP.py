# cook your dish here


def solve():
    def prime(X):
        if X == 2 or X == 3:
            return True
        if X == 1 or X % 2 == 0 or X % 3 == 0:
            return False
        for i in range(5, int(X**0.5) + 2, 6):
            if X % i == 0 or X % (i + 2) == 0:
                return False

        return True
    def sol(N, X, A):
        if prime(X):
            try:
                i = A.index(1, 0) + 1
                j = A.index(1, i) + 1
                k = A.index(1, j) + 1
                l = A.index(X, 0) + 1
                return sorted([i, j, k, l])
            except ValueError:
                return [-1]

        if X == 0:
            try:
                i = A.index(0) + 1
                if i in [1, 2, 3, 4]:
                    return [1, 2, 3, 4]
                else:
                    return [1, 2, 3, i]
            except ValueError:
                return [-1]

        for i in range(N):
            if A[i] and not X % A[i]:
                for j in range(i + 1, N):
                    if A[j] and not X % A[j]:
                        for k in range(j + 1, N):
                            if A[k] and not X % A[k]:
                                for l in range(k + 1, N):
                                    if A[l] and not X % A[l] and A[i]*A[j]* A[k]*A[l]==X:
                                        return [i+1, j+1, k+1, l+1]
        return [-1]


    for _ in range(int(input())):
        N, X = map(int, input().split())
        A = list(map(int, input().split()))

        print(*sol(N, X, A))


if __name__ == "__main__":
    solve()
