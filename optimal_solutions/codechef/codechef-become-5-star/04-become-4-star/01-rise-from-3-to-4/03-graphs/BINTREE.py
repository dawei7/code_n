


def solve():
    for _ in range(int(input())):
        n1,n2=map(int,input().split())
        count=0
        while(n1!=n2):
            if(n1>n2):
                n1//=2
            else:
                n2//=2
            count+=1
        print(count)


if __name__ == "__main__":
    solve()
