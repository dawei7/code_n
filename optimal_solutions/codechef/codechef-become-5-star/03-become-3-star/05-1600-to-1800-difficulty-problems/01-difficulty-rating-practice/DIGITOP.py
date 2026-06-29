


def solve():
    for _ in range(int(input())):
        n,x=map(int,input().split())
        a=list(map(str,input().split()))
        b=list(map(str,input().split()))
        aa={}
        bb={}
        ans=0
        for i in range(n):
            if len(a[i])!=len(b[i]):
                ans=1
                break
            else:
                for j in range(len(a[i])):
                    if a[i][j] not in aa:
                        aa[a[i][j]]=1
                    else:
                        aa[a[i][j]]+=1
                    if b[i][j] not in bb:
                        bb[b[i][j]]=1
                    else:
                        bb[b[i][j]]+=1
        if ans:
            print("NO")
        else:
            abcd=0
            ans=1
            for k in aa:
                if abcd>x:
                    ans=0
                    break
                else:
                    if k in bb:
                        if aa[k]-bb[k]>0:
                            abcd+=aa[k]-bb[k]
                    else:
                        abcd+=aa[k]
            #print(aa,bb,abcd)
            if abcd>x:
                ans=0
            if ans:
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    solve()
