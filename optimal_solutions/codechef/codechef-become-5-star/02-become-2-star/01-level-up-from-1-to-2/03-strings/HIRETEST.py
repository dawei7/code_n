# cook your dish here


def solve():
    for i in range(int(input())):
        a,b=map(int,input().split())
        x,y=map(int,input().split())
        l=[]
        s=''
        for i in range(a):
            l.append(input())
        for i in l:
            if i.count('F')>=x or(i.count('F')>=(x-1) and (i.count('P')>=y)):
                s+='1'
            else:
                s+='0'
        print(s)


if __name__ == "__main__":
    solve()
