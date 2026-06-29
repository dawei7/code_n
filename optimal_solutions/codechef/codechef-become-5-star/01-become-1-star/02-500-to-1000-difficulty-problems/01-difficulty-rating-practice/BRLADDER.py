# cook your dish here
import math


def solve():
    def find_max(a,b):
        if(a>b):
            return a
        else:
            return b

    t=int(input())
    for i in range(t):
        a,b=map(int,input().split())
        if(a%2==0 and b%2==0 and abs(a-b)==2):
            print("YES")
        elif(a%2!=0 and b%2!=0 and abs(a-b)==2):
            print("YES")
        else:
            maxi=find_max(a,b)
            if(maxi%2==0 and abs(a-b)==1):
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    solve()
