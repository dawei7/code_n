


def solve():
    t=int(input())
    for i in range(t):
        n,m,x = [int(i)for i in input().split()]
        a = [int(i)for i in input().split()]
        count = 0
        b=[]
        c=[]
        for i in range(len(a)):
            if a[i]>=m:
                count+=1
                b.append(a[i])
            else:
                c.append(a[i])
        if count>=x:
            print(count,end = " ")        
            for i in a:
                if i in b:
                    print(a.index(i)+1,end = " ")
        else:
            while(count<x):
                b.append(max(c))
                c.remove(max(c))
                count+=1
            print(count,end = " ")   
            for i in a:
                if i in b:
                    print(a.index(i)+1,end = " ")

        print("")


if __name__ == "__main__":
    solve()
