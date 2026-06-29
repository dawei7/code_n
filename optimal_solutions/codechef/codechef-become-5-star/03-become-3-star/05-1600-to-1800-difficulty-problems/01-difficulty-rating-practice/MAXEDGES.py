import math


def solve():
    for _ in range(int(input())):
        n,k,l=[int(x) for x in input().split()]
        mid=0
        if k+l<n:
            mid=n-(k+l)
        elif k+l>n:
            temp=k+l-n
            k-=temp
            l-=temp

        res=(k*(mid+l))+(mid*l)
        if mid>1:
            res+=(mid*(mid-1))//2
        print(res)


if __name__ == "__main__":
    solve()
