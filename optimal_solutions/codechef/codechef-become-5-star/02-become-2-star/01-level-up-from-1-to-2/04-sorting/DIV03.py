# cook your dish here


def solve():
    for _ in range(int(input())):
        a=list(map(int,input().split()))
        b=int(input())
        c=a[::-1]
        d=0
        for x in c:
            if x<=b:
                d+=1
                b=b-x
            else:
                break
        print(10-d)


if __name__ == "__main__":
    solve()
