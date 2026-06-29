# www.codechef.com/problems/RACINGEN


def solve():
    T = int(input())
    for _ in range(T):
        X, R, M = map(int, input().split())
        R *= 60
        M *= 60
        time_taken = max(R, 2 * R - X)
        if time_taken <= M:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
