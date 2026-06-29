import math


def solve():
    t = int(input())
    for i in range(0,t):
        N = int(input())
        see = 0
        for j in range(N):
            P,Q,D = map(int,input().split())
            temp = (D*P)/100
            tem = P + temp
            kemp = (D*tem)/100
            kem = tem - kemp
            see += (P-kem)*Q
        print(round(see,9))


if __name__ == "__main__":
    solve()
