


def solve():
    for i in range(int(input())):
        a=int(input())
        b=list(map(int,input().split()))

        c=0
        for j in range(len(b)-1):
            if b[j]>b[j+1]:
                b[j+1],b[j]=b[j],b[j+1]
                break
        if b!=sorted(b):
            print("NO")

        else:
            print("YES")


if __name__ == "__main__":
    solve()
