import math


def solve():
    t = int(input())

    while(t>0):
        x = int(input())
        start = x
        end = 10**10
        mid = (start+end)//2
        ans = 10**20
        while(start<=end):
            sq = mid
            zz = mid*mid
            cb = int(zz**(1/3))
            val = cb+1
            val = val**3
            if(val == zz):
                cb+=1;

            dif = sq - cb


            if(dif>=x):
                ans = min(ans,zz)
                end = mid-1
                mid = (start+end)//2
            else:
                start = mid+1
                mid = (start+end)//2

        print(ans)
        t-=1


if __name__ == "__main__":
    solve()
