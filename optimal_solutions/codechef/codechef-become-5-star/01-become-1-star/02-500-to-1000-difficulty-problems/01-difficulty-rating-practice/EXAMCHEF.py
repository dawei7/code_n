# cook your dish here


def solve():
    t=int(input())

    for i in range(t):

        x,y,z=map(int,input().split())

        s=x*y

        per=(z/s)*100 #per=value/total_value*100

        if per>50:
            print('yes')

        else:
            print('no')


if __name__ == "__main__":
    solve()
