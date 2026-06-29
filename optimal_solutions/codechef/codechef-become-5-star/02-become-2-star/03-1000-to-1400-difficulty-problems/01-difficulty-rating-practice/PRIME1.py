import sys
import math


def solve():
    def is_prime(num):
        if num<=1:
            return False
        if num<=3:
            return True
        if num%2==0 or num%3==0:
            return False
        i=5
        while i*i<=num:
            if num%i==0 or num%(i+2)==0:
                return False
            i+=6
        return True
    t=int(input())
    for _ in range(t):
        m,n=map(int,input().split())
        for i in range(m,n+1):
            if(is_prime(i)):
                print(i)
        if _ <t-1:
            print()


if __name__ == "__main__":
    solve()
