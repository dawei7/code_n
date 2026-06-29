


def solve():
    for _ in range(int(input())):
        n,k=map(int,input().split())
        s=input()
        li=[]
        bcount=0
        for i in range(n-1,-1,-1):
            if(s[i]=='b'):
                bcount+=1 
            li.append(bcount)
        li.reverse()
        total=0
        for i in range(n):
            if(s[i]=='a'):
                total+=li[i]*k 
                total+=((k*(k-1))//2)*bcount 
        print(total)


if __name__ == "__main__":
    solve()
