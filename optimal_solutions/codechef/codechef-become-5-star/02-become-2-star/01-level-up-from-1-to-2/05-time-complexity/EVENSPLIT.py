# cook your dish here


def solve():
    t=int(input())
    while(t):
        count=0
        n=int(input())
        s=input()
        l=[]
        if(n>2):
            for i in s:
                if(i=='0'):
                    print(i,end="")
                else:
                    count=count+1
            for i in range(count):
                print(1,end='')
            print()
        else:
            print(s)
        t=t-1


if __name__ == "__main__":
    solve()
