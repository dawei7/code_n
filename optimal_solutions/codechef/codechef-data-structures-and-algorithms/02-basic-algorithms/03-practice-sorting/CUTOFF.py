


def solve():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        a = list(map(int, input().split()))
        ans = 0
        for i in range(101):
            passed = 0
            for y in a: passed += y > i
            if passed >= x: ans = i
        print(ans)


if __name__ == "__main__":
    solve()
