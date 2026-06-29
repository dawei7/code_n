# cook your dish here


def solve():
    tst=int(input())
    for i in range(tst):
        count=0
        n,min_age=map(int,input().split())
        people=list((map(int,input().split())))
        for per in people:
            if per>=min_age:
                count+=1 
        print(count)


if __name__ == "__main__":
    solve()
