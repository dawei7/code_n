# cook your dish here
import math


def solve():
    t=int(input())
    while(t!=0):
        n=int(input())
        temp=10**(n-1)
        temp1=10**n
        for i in range(temp,temp1):
            if(i%3==0 and i%9!=0 and i%2!=0):
                print(i)
                break
        t-=1


if __name__ == "__main__":
    solve()
