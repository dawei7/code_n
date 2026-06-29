import sys


def solve():
    class Codechef:
        def main():
            # Reading input
            input_data = sys.stdin.read().splitlines()
            first_line = input_data[0].split()
            N = int(first_line[0])  # Number of items
            W = int(first_line[1])  # Weight limit
            L = int(first_line[2])  # Length limit

            A = []
            for i in range(N):
                a, b = map(int, input_data[i + 1].split())
                A.append((a, b))

            l = 0
            h = 10**18
            result = Codechef.binary_search(l, h, A, W, L)
            print(Codechef.clean(result, A, W, L))

        def ok(m, A, W, L):
            s = 0

            for i in range(len(A)):
                if A[i][0] + m * A[i][1] >= L:
                    s += A[i][0] + m * A[i][1]

                if s >= W:
                    return True
            return s >= W

        def clean(k, A, W, L):
            for m in range(k - 1, k + 2):
                if 0 <= m <= 10**18 and Codechef.ok(m, A, W, L):
                    return m
            return k

        def binary_search(l, h, A, W, L):
            while l < h:
                m = (l + h) // 2

                if Codechef.ok(m, A, W, L):
                    h = m - 1
                else:
                    l = m + 1
            return l

    if __name__ == "__main__":
        Codechef.main()


if __name__ == "__main__":
    solve()
