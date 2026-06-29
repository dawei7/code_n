


def solve():
    for distractions in range(int(input())):
        aim, wife, life = map(int, input().split())
        if wife % life == 0 or (aim + 1 - wife) % life == 0:
            print('YES')
        else:
            print('NO')


if __name__ == "__main__":
    solve()
