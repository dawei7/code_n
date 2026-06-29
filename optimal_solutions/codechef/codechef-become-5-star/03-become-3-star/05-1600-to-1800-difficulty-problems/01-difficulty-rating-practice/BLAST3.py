from collections import *


def solve():
    t = int(input())
    def check(l,r):
        L = []
        R = []
        for i in range(l,n+1,3):
            L += [s[i-1]]
        for i in range(r,n+1,3):
            R += [s[i-1]]
        flag = False
        C = Counter(R)
        for i in range(len(L)):
            a = L[i]
            if a in C:
                flag = True
                break
            C[R[i]] -= 1
            if C[R[i]]==0:
                del C[R[i]]
        print("YES" if flag else "NO")
    for _ in range(t):
        n = int(input())
        s = input()
        if s==s[::-1]:
            print("YES")
        elif n<=3:
            print("NO")
        elif n%3==1:
            print("YES")
        elif n%3==2:
           check(1,2)
        else:
            check(1,3)


if __name__ == "__main__":
    solve()
