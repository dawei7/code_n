# cook your dish here
# cook your dish here
import math


def solve():
    t=int(input())
    for i in range(t):
        s=input()
        n=len(s)
        dp=[0]*26
        for ch in s:
            ind=ord(ch)-ord('A')
            dp[ind]+=1
        cnt=0
        for i in dp:
            cnt+=i!=0
        ans=n-max(dp)
        dp.sort(reverse=True)
        for i in range(2,27):
            if(n%i!=0):
                continue
            summ=0
            for j in range(i):
                summ+=max(0,n//i-dp[j])
            ans=min(ans,summ)
        print(ans)


if __name__ == "__main__":
    solve()
