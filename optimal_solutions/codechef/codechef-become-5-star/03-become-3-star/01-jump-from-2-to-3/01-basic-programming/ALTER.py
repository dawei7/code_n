


def solve():
    for _ in range(int(input())):
        a, b, p, q = map(int, input().split())
        if a > p or b > q:
            print("NO")
        elif p % a == 0 and q % b == 0:
            print("YES") if abs(p // a - q // b) <= 1 else print("NO")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
