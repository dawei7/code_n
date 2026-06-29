# cook your dish here


def solve():
    for _ in range(int(input())):
        x=int(input())
        flag=0
        while(x>=0):
            if(x%7==0):
                print(x)
                flag=1
                break
            x-=4
        if not flag:
            print(-1)


if __name__ == "__main__":
    solve()
