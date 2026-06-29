# cook your dish here


def solve():
    for i in range(int(input())):
        n,x = map(int,input().split())

        if n < (2*x)-1:
            print(-1)

        else:
            alpha = 'abcdefghijklmnopqrstuvwxyz'
            part1 = alpha[:x]
            repeat = n - ( 2*len(part1) )
            start = 0
            if repeat < 0:
                start = 1

            print(part1 + repeat*part1[-1] + part1[::-1][start:])


if __name__ == "__main__":
    solve()
