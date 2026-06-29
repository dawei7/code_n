# cook your dish here


def solve():
    for t in range(int(input())):
        length=int(input())
        fs=input()
        ss=input()
        tf=input()
        ans=""
        if(ss[0]>fs[0]):
            diff=ord(ss[0])-ord(fs[0])
            for k in range(length):
                if(ord(tf[k])+diff>122):
                    ans=ans+chr((ord(tf[k])+diff)-26)
                else:
                    ans=ans+chr((ord(tf[k])+diff))
        elif(ss[0]<fs[0]):
            diff=ord(fs[0])-ord(ss[0])
            for k in range(length):
                if(ord(tf[k])-diff<97):
                    ans=ans+chr((ord(tf[k])-diff)+26)
                else:
                    ans=ans+chr((ord(tf[k])-diff))
        else:
            print(tf)
        print(ans)


if __name__ == "__main__":
    solve()
