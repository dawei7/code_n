


def solve():
    t=int(input())
    for i in range(t):
        n=int(input())
        l=[]
        for i in range(n):
            s=input()
            s=set(list(s))
            l.append(s)
        a=l[0]
        for i in l[1:]:
            a=a.intersection(i)
        print(len(a))


if __name__ == "__main__":
    solve()
