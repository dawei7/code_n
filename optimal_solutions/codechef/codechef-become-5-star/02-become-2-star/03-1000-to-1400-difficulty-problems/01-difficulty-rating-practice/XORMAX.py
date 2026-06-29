# Online Python compiler (interpreter) to run Python online.
# cook your dish here


def solve():
    for i in range(int(input())):
        a=input()
        b=input()
        s=o=0
        for i in range(len(a)):
            if(a[i]=='0'):
                s+=1
            else:
                o+=1
            if(b[i]=='0'):
                s+=1
            else:
                o+=1
        m=min(s,o)
        sr=""
        for i in range(0,m):
            sr+='1'
        for i in range(m,len(a)):
            sr+='0'
        print(sr)


if __name__ == "__main__":
    solve()
