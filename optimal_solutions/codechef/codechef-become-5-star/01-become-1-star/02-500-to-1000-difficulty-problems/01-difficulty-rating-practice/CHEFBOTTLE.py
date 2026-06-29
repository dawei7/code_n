# cook your dish here


def solve():
    T = int(input())
    for i in range(T):
        N, X, K = map(int, input().split())
        A = K // X
        print(min(N, A))


if __name__ == "__main__":
    solve()
