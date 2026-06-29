# cook your dish here


def solve():
    for _ in range(int(input())):
        s=sorted(input())
        n=len(s)
        res=0
        for i in range(n):
            res+=(i+1)*(ord(s[i])-96)
        print(res)


if __name__ == "__main__":
    solve()
