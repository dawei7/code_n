# cook your dish here

from math import gcd


def solve():
    for T in range(int(input())):

        N,M = map(int,input().strip().split())
        total_value = N*(N+1)//2

        if M > total_value:
            print("No")

        elif total_value % 2 != M % 2:
            print("No")

        else:
            A = (total_value-M)//2
            B = total_value - A

            if gcd(A,B) != 1:
                print("No")
            else:
                print("Yes")


if __name__ == "__main__":
    solve()
