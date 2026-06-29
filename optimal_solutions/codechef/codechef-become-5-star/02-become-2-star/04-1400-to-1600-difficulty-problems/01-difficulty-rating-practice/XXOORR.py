# cook your dish here
import math


def solve():
    for _ in range(int(input())):
        n,k=map(int,input().split())
        l=list(map(int,input().split()))
        ans=0
        for i in range(32):
            cnt=0
            for j in l:
                if(j>>i&1==1):
                    cnt+=1
            ans=ans+math.ceil(cnt/k)
        print(ans)


if __name__ == "__main__":
    solve()
