


def solve():
    k=int(input())
    for i in range(k):
        a=list(map(int,input().split()))
        if a[0]*a[1]<=a[2]*a[3]:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    solve()
