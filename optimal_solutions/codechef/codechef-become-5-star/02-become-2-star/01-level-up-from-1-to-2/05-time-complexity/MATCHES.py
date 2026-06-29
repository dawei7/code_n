


def solve():
    t=int(input())
    for i in range(t):
        a,b=map(int,input().split())
        dic={'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,
        '7':3,'8':7,'9':6}
        c=a+b
        c=str(c)
        ans=0
        for i in c:
            ans+=dic[i]
        print(ans)


if __name__ == "__main__":
    solve()
