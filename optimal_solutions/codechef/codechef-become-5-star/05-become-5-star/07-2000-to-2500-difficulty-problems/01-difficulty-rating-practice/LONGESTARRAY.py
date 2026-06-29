import sys
from math import *
from collections import *


def solve():
    inp = lambda: sys.stdin.buffer.readline().decode().strip()
    out=sys.stdout.write
    # n=int(inp())
    # arr=list(map(int,inp().split()))
    for _ in range(int(inp())):
        n=int(inp())
        arr=list(map(int,inp().split()))
        xor=[[0]*32 for _ in range(n)]
        cnt=[0]*32
        for i,num in enumerate(arr):
            for idx in range(32):
                if num & (1<<idx):
                    xor[i][idx]=1
                    cnt[idx]+=1
        flag=True
        for i in range(32):
            if cnt[i]==1:
                flag=False
                break
        if not flag: 
            print(-1)
            continue
        mmax=-1
        i,j=0,0
        sub_xor,rest_xor=[0]*32,[x for x in cnt]
        while j<n:
            gg=0
            for idx in range(31,-1,-1):
                if rest_xor[idx]==0 and sub_xor[idx]>0:
                    gg=1
                    #keep evaluating ith index out of subarray into rest until condition is True
                    while i<=j and (arr[i] & (1<<idx))==0: 
                        sub_xor=[num-val for num,val in zip(sub_xor,xor[i])]
                        rest_xor=[num+val for num,val in zip(rest_xor,xor[i])]
                        i+=1
                    if i<=j:
                        sub_xor=[num-val for num,val in zip(sub_xor,xor[i])]
                        rest_xor=[num+val for num,val in zip(rest_xor,xor[i])]
                        i+=1
                    if i>=j:
                        i,j=j+1,j+1
                    break
            if gg==0:
                #evaluate jth index into subarray
                sub_xor=[num+val for num,val in zip(sub_xor,xor[j])]
                rest_xor=[num-val for num,val in zip(rest_xor,xor[j])]
                j+=1

            flag=True
            for ii in range(32):
                if (sub_xor[ii]>0 and rest_xor[ii]==0) or (sub_xor[ii]==0 and rest_xor[ii]>0):
                    flag=False
                    break
            if flag: 
                # print(i,j-1,sub_xor[:4],rest_xor[:4])
                mmax=max(mmax,j-i)
        print(mmax)


if __name__ == "__main__":
    solve()
