from math import gcd


def solve():
    for _ in range(int(input())):
        n, k = [int(i) for i in input().split()]
        ai = input().split()
        g = int(ai[0])
        for i in ai[1:]:
            g = gcd(g, int(i))
        c = 0
        newG = 0
        for i in ai:
            newG = gcd(newG, int(i))
            if newG == g:
                c += 1
                newG = 0
                if c == k:
                    break
        if c == k:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
