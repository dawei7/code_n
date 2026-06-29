


def solve():
    t=int(input())
    for _ in range(t):
        n=input()
        l=[int(x) for x in n]
        s=sum(l)
        temp=int(n)+1
        while True:
            temp=str(temp)
            l2=[int(x) for x in temp]
            if sum(l2)%2!=s%2:
                print(temp)
                break
            else:
                temp=int(temp)+1


if __name__ == "__main__":
    solve()
