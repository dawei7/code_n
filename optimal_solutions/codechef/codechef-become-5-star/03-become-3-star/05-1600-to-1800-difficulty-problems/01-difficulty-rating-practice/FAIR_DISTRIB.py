


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        pre = [0] * n
        suf = [0] * n
        c = 0
        for i in range(n):
            if s[i]=='1':
                c += 1
            pre[i] = c
        c = 0
        for i in range(n-1,-1,-1):
            if s[i]=='1':
                c += 1
            suf[i] = c
        A = pre[-1] * n
        B = (n - pre[-1]) * n
        flag = True
        if abs(A-B)>n:
            flag = False
        for i in range(n):
            if s[i]=='1':
                A -= n
            else:
                B -= n
            if abs(A-B)>n:
                flag = False
        print("YES" if flag else "NO")


if __name__ == "__main__":
    solve()
