# cook your dish here


def solve():
    for _ in range(int(input())):
        n,k=map(int,input().split())
        s=input()
        c=0
        for i in s:
            if c==k:
                break
            if i=='*':
                c+=1
            else:
                c=0
        if c>=k:
            print('YES')
        else:
            print('NO')


if __name__ == "__main__":
    solve()
