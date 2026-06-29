


def solve():
    for _ in range(int(input())):
    	n, m, x, y = map(int, input().split())
    	print('yes' if x%2 == (n+m)%2 or y%2 == (n+m)%2 else 'no')


if __name__ == "__main__":
    solve()
