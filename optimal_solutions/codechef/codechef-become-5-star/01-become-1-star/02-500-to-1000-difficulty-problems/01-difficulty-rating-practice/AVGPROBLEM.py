# cook your dish here


def solve():
    for t in range(int(input())):
        a,b,c = map(int,input().split())
        if(((a+b)/2)>c):
            print("yes")
        else:
            print('no')


if __name__ == "__main__":
    solve()
