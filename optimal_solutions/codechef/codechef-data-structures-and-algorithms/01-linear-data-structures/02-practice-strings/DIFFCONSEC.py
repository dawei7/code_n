# cook your dish here


def solve():
    for i in range(int(input())):
        N=int(input())
        s=input()
        c=0
        for i in range(N-1):
            if(s[i]==s[i+1]):
                c+=1
        print(c)


if __name__ == "__main__":
    solve()
