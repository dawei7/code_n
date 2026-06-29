


def solve():
    t=int(input())
    for i in range(t):
        n=int(input())
        s=input()
        if ('H' not in s) and ('T' not in s):
                 print("Valid")
        else:
            l=[]
            c=0
            for j in s:
                if j=='H' or j=='T':
                    l.append(j)
            if l.count('H')!=l.count('T'):
                print("Invalid")
            else:
                for k in range(0,len(l),2):
                    if(l[k]=='H' and l[k+1]=='T'):
                        c+=2
                if(c==len(l)):
                    print("Valid")
                else:
                    print("Invalid")


if __name__ == "__main__":
    solve()
