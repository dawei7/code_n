


def solve():
    t=int(input())
    j=0
    for i in range(t):
        a,b,c,d,k=map(int,input().split(" "))
        j=abs(c-a)+abs(d-b)
        if(j==k):
            print("Yes")
        elif((j-k)%2==0 and j<k):
            print("Yes")
        elif(j>k):
            print("No")
        else:
            print("No")


if __name__ == "__main__":
    solve()
