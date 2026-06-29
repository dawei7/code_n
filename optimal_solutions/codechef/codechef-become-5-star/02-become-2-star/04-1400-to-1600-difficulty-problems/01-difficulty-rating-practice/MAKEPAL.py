import math


def solve():
    for _ in range(int(input())):
        n=int(input())
        l=list(map(int,input().split()))
        odd=0;
        for i in l:
            if(i&1==1):
                odd+=1;
        print(int(math.floor(odd/2)))


if __name__ == "__main__":
    solve()
