# cook your dish here


def solve():
    t = int(input())
    for _ in range(t):
        res = 1
        n,m,l = map(int, input().split())
        if(n == 1 or m == 1 or l == 1):
            q = input()
            x = input()
            print(res)
            continue
        l1 = [0]*(n+1)
        for i in range(m):
            s = list(map(int,input().split()))
            for j in range(1,len(s)):
                l1[s[j]] = i
        str1 = list(map(int,input().split()))
        for i in range(1, len(str1)):
            if(l1[str1[i]] != l1[str1[i-1]]):
                res=res+1
        print(res)


if __name__ == "__main__":
    solve()
