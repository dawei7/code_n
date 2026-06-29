


def solve():
    def check(l,n):
        for i in range(1,n):
            if l[i-1]>l[i]:
                return False
        return True

    # cook your dish here
    for _ in range(int(input())):
        n = int(input())
        l = list(map(int,input().split()))
        s = input()
        cn, cs = 0,0
        for i in s:
            cn |= i=="N"
            cs |= i=="S"

        templ = l[:]
        if check(templ, n):
            print(0)
            continue

        if not cn or not cs:
            print(-1)
            continue

        if s[0] != s[-1]:
            print(1)
            continue

        templ = l[:]

        ptr = 0
        while(s[ptr]==s[0]): ptr+=1
        templ[ptr:] = sorted(templ[ptr:])
        if check(templ,n):
            print(1)
            continue

        templ = l[:]

        ptr = n-1
        while(s[ptr]==s[-1]): ptr-=1
        templ[: ptr+1] = sorted(templ[: ptr+1])
        if check(templ,n):
            print(1)
            continue

        print(2)


if __name__ == "__main__":
    solve()
