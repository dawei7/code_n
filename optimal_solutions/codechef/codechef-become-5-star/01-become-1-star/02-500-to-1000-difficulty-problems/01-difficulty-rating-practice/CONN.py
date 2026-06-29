


def solve():
    t=int(input())
    for _ in range(t):
        N=int(input())
        if N>=7:
            print('YES')
        else:
            if N%2==0:
                print('YES')
            else:
                print('NO')


if __name__ == "__main__":
    solve()
