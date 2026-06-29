


def solve():
    for _ in range(int(input())):
        n = int(input())
        s = input()
        assert len(s) == n
        n_moves = min(s.count('0'), s.count('1'))
        print('Zlatan' if n_moves % 2 == 1 else 'Ramos')


if __name__ == "__main__":
    solve()
