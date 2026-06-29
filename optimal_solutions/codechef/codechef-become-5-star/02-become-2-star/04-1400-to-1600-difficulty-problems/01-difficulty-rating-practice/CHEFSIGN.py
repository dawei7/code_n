


def solve():
    t = int(input())

    for _ in range(t):
        s = input().replace("=","")

        if s!= "":
            p = s[0]

        n,m = 0,0

        for i in s:
            if i==p:
                n+=1
                m = max(m,n)
            else:
                n = 1
                p = i

        print(m+1)


if __name__ == "__main__":
    solve()
