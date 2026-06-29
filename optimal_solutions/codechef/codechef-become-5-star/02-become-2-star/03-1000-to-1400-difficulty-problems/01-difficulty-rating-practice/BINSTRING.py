# cook your dish here


def solve():
    for _ in range(int(input())):
        n=int(input())
        b=input()
        c=''
        d=0
        for i in b:
            if i==c:
                continue
            c=i
            d+=1
        print(d)


if __name__ == "__main__":
    solve()
