# cook your dish here


def solve():
    for _ in range(int(input())):
        n,w=input().split()
        n,w=int(n),int(w)
        l=[]
        dp=[]
        for i in range(n):
            l.append(list(map(int,input().split())))
            dp.append([-1 for i in range(w+1)])

        def f(i,w):
            if w<=0 or i>=n:
                return 0
            if dp[i][w]!=-1:
                return dp[i][w]
            pick=0
            if(w-l[i][2]>=0):
                pick=l[i][0]*l[i][1] + f(i+1,w-l[i][2])
            notpick=f(i+1,w)
            dp[i][w]=max(pick,notpick)
            return dp[i][w]

        print(f(0,w))


if __name__ == "__main__":
    solve()
