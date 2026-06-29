


def solve():
    for _ in range(int(input())):
        n,w=map(int,input().split())
        l=sorted(list(map(int,input().split())))
        c=0
        for j in range(n-1,-1,-1):
            c+=l[j]
            if c>=w:
                print(j)
                break
        else:
            print(0)


if __name__ == "__main__":
    solve()
