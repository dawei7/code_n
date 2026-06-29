# cook your dish here


def solve():
    for t in range(int(input())):
        b=int(input())
        f=[]
        for g in range(1,b+1):
            if g%2==0:
                f.append(f[-1]*2)
            else:
                f.append(g)
        print(*f)


if __name__ == "__main__":
    solve()
