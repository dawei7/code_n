from math import gcd


def solve():
    for _ in range(int(input())):
        len_arr=int(input())
        arr=list(map(int,input().split()))
        if len_arr==1:
            print(arr[0])
        else:
            gcd_val=gcd(arr[0],arr[1])
            for index in range(2,len_arr):
                gcd_val=gcd(gcd_val,arr[index])
            print(gcd_val)


if __name__ == "__main__":
    solve()
