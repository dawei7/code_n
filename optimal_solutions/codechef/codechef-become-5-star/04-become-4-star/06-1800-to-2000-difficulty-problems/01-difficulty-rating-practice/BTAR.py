from collections import Counter


def solve():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(lambda x: int(x) % 4, input().split()))
        c = Counter(a)

        ans = min(c[1], c[3])
        c[1], c[3] = c[1]-ans, c[3]-ans

        if (c[1]%2 == 1) or (c[3]%2 == 1):
            print(-1)

        else:
            c[2] += (c[1]//2 + c[3]//2) #one of them will be 0
            ans += (c[1]//2 + c[3]//2)
            if c[2] % 2 == 1:
                print(-1)
            else:
                ans += c[2]//2
                print(ans)


if __name__ == "__main__":
    solve()
