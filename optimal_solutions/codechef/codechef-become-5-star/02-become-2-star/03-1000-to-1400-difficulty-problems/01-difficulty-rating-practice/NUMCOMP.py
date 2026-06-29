# cook your dish here
# cook your dish here


def solve():
    T = int(input())

    for tc in range (T):
        a,b,n = map(int, input().split())
        if (n%2==0):
            if(abs(a)>abs(b)):
                print(1)
            elif(abs(a)<abs(b)):
                print(2)
            else:
                print(0)
        else:
            if(a>b):
                print(1)
            elif(a<b):
                print(2)
            else:
                print(0)


if __name__ == "__main__":
    solve()
