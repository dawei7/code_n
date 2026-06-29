# cook your dish here
import math


def solve():
    def Solve(s):
        zeros=0
        i=len(s)-1
        while(i>=0 and s[i]=='0'):
            zeros+=1
            i=i-1
        if(i==0 and s[0]=='1'):
            return "Yes"
        value=int(s[:i+1])
        x=math.log(value,2)
        if(2**x==value):
            if(zeros>=x):
                return "Yes"
        return "No"

    for _ in range(int(input())):
        n=input()
        print(Solve(n))


if __name__ == "__main__":
    solve()
