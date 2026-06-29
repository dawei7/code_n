def te():
    n_sum = 0
    n = int(input())
    n_sum += n
    assert n_sum <= 200 * 1000
    t = list(map(int, input().split()))
    t.sort()
    for i in range(n - 1):
        if t[i] + 1 < t[i + 1]:
            print('NO')
            return
    print('YES')

def solve():
    T = int(input())
    for _ in range(T):
        te()


if __name__ == "__main__":
    solve()
