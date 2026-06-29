# cook your dish here
import math


def solve():
    for _ in range(int(input())):
        x=int(input())
        k=math.sqrt(2*x+1/4)-1/2;
        ceil,floor=math.ceil(k),math.floor(k)
        sum_max,sum_min=ceil*(ceil+1)//2,floor*(floor+1)//2
        print(min(floor+abs(x-sum_min),ceil+abs(sum_max-x)))


if __name__ == "__main__":
    solve()
