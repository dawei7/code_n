


def solve():
    for _ in range(int(input())):
        n=int(input())
        a=list(map(int,input().split()))

        a.sort()
        count=0
        if a[n//2]==a[n//2-1]:
            count = a[:n//2].count(a[n//2])
        if n%2!=0:
            count+=1 
        print(n//2+count)


if __name__ == "__main__":
    solve()
