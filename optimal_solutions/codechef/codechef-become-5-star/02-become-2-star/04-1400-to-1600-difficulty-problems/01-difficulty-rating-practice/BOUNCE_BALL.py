


def solve():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        s_r = sum(a)
        s_l = 0
        ans = 0
        for x in a:
            s_r -= x
            if x == 0:
               if s_l == s_r: ans+=2
               elif abs(s_l - s_r) == 1: ans+= 1
            s_l += x
        print(ans)


if __name__ == "__main__":
    solve()
