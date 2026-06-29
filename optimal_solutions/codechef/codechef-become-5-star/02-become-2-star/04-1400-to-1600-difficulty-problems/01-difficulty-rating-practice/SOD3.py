# cook your dish here
import math;


def solve():
    for _ in range(int(input())):
        l,r=map(int,input().split());
        p1,p2=math.ceil(l/3),math.floor(r//3);
        print(int(p2-p1+1));


if __name__ == "__main__":
    solve()
