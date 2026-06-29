# cook your dish here


def solve():
    for _ in range(int(input())):
        n, k = map(int,input().split())
        arr = list(map(int,input().split()))
        # arr.sort()
        d = max(arr)
        e = min(arr)
        # print(d)
        if n==1:
            print("YES")
        elif d>k:
            print("NO")
        elif d + e<=k:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
