# cook your dish here


def solve():
    for _ in range(int(input())):
        s=input()
        c='0'
        o='1'
        m=0
        for i in s:
            if i==c:
                c,o=o,c
                m+=1
        print(m)


if __name__ == "__main__":
    solve()
