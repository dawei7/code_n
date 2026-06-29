# cook your dish here


def solve():
    for i in range(int(input())):
        n = int(input())
        a = list(map(int,input().split()))
        b = 0
        c = 0
        for i in a:
            if i%2 == 0:
                b += 1
            else:
                c += 1
        print(b*c)


if __name__ == "__main__":
    solve()
