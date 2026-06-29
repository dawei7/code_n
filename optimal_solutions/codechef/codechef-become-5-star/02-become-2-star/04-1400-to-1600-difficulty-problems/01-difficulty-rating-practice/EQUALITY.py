# cook your dish here


def solve():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        sum =0
        for i in arr:
            sum+=i
        d= int(sum /(n-1))
        for i in range(n):
            print(d-arr[i], end=" ")
        print('')


if __name__ == "__main__":
    solve()
