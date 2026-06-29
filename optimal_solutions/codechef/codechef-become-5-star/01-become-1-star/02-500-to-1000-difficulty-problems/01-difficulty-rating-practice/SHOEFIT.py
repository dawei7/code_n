# cook your dish here


def solve():
    for _ in range(int(input())):
        a,b,c=map(int,input().split())
        if a==b and b==c:
            print('0')
        else:
            print('1')


if __name__ == "__main__":
    solve()
