# cook your dish here


def solve():
    for i in range(int(input())):
        s=input()
        s1=s[1:]+s[0]
        s2=s[-1]+s[:-1]
        if s1==s2:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
