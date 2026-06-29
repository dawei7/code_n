


def solve():
    t=int(input())
    for i in range(t):
        n, k = map(int, input().split())
        coins = list(map(int, input().split()))
        total = 0    
        for a in coins:
            total += a
        print(total % k)


if __name__ == "__main__":
    solve()
