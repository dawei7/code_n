# cook your dish here
# cook your code here


def solve():
    a=int(input())
    for i in range(a):
        b=int(input())
        d=input()
        c=0
        for i in d:
            c=d.count(i)
            if(c%2==0):
                c=0
            else:
                c=1
                break 
        if(c!=0):
            print("NO")
        else:
            print("YES")


if __name__ == "__main__":
    solve()
