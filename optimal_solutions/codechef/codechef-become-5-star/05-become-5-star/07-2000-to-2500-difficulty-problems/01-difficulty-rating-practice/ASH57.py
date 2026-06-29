from collections import *
import bisect


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = list(map(int,input().split()))
        CA = list(map(int,input().split()))
        B = list(map(int,input().split()))
        CB = list(map(int,input().split()))
        X = defaultdict(list)
        Y = defaultdict(list)
        for i in range(n):
            X[CA[i]] += [A[i]]
            Y[CB[i]] += [B[i]]
        D = defaultdict(list)
        R = defaultdict(list)
        for i in X:
            if i in Y:
                D[i] = sorted(X[i]+Y[i])
            else:
                R[i] = X[i]
        for i in Y:
            if i not in X:
                R[i] = Y[i]
        ans = []
        for i in range(n):
            a = CA[i]
            if a in D:
                ans += [(a,i)]
            else:
                ans += [(R[a].pop(0),'-')]
        st = []
        prev = 0
        res = []
        flag = True
        # print('D',D)
        # print('R',R)
        # print('ans',ans)
        for i in range(n):
            if ans[i][1]=='-':
                prev = ans[i][0]
                res += [ans[i][0]]
            else:
                while D[ans[i][0]] and D[ans[i][0]][0]<prev:
                    D[ans[i][0]].pop(0)
                if D[ans[i][0]]:
                    res += [D[ans[i][0]].pop(0)]
                    prev = res[-1]
                else:
                    res += [-1]
                    flag = False
                    prev = float('inf')
        # print('res',res)
        if sorted(res)==res and flag:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    solve()
