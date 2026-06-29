from sys import stdin


def solve():
    input = stdin.readline

    T = int(input())
    for tx in range(T):
        N = int(input())
        S = input().strip().split(")")
        cl = len(S)-1
        op = 0
        for sp in S:
            op += len(sp)
            if op >= cl:
                break
            cl -= 1
        print(N-2*cl)


if __name__ == "__main__":
    solve()
