# cook your dish here
# cook your dish here


def solve():
    for _ in range(int(input())):
        n=int(input())
        l=list(map(int,input().split()))
        for i in range(n):
            if((i+1)%l[i]==0):
                continue
            else:
                print("NO")
                break
        else:
            print("YES")


if __name__ == "__main__":
    solve()
