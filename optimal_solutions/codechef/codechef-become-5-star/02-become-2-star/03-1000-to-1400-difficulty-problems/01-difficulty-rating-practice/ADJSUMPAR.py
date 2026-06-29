# cook your dish here


def solve():
    for i in range(int(input())):
        a=int(input())
        s=input()
        c=s.count('1')
        if(c%2==0):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
