# cook your dish here


def solve():
    N=int(input())
    a=list(map(int,input().split()))
    e=0
    o=0
    for i in a:
            if i%2==0:
                e+=1# -*- coding: latin-1 -*-
            else:
                o+=1

    if e>o:
            print("READY FOR BATTLE")
    else:
            print("NOT READY")


if __name__ == "__main__":
    solve()
