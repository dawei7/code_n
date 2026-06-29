# www.codechef.com/problems/LINCHESS


def solve():
    T = int(input())
    for prob in range(T):
        N, K = map(int, input().split())
        players = list(map(int, input().split()))

        min_moves = K + 1
        result = -1
        for cand in players:
            if K % cand == 0:
                moves = K // cand - 1
                if moves < min_moves:
                    min_moves = moves
                    result = cand

        print(result)


if __name__ == "__main__":
    solve()
