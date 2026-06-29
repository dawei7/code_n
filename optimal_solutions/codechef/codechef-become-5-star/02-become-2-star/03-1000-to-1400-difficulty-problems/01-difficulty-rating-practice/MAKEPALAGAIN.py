


def solve():
    for i in range(int(input())):
        n=int(input())
        s=input()
        s1 , s2=s[::2],s[1::2]
        # print(a,b)
        s1 = sorted(s1)
        s2 = sorted(s2)
        if s1==s2:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
