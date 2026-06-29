


def solve():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        if n%2 == 1:
            print('Chef' if sum(a)%2 == 1 else 'Chefina')
        else:
            S, M = sum(a), min(a)
            print('Chef' if S%2 == 1 or M%2 == 1 else 'Chefina')


if __name__ == "__main__":
    solve()
