# cook your dish here


def solve():
    for sfnsj in range(int(input())):
        n=int(input())
        sn=bin(n).replace("0b", "")
        #print(sn)
        a=""
        b=""
        c=0
        for i in sn:
            if(i=='1'):
                if(c==0):
                    a+='1'
                    b+='0'
                else:
                    a+='0'
                    b+='1'
            elif(i=='0'):
                a+='1'
                b+='1'
                #k=False
            c+=1
        #print(a,b)
        a=int(a,2)
        b=int(b,2)
        print(a*b)


if __name__ == "__main__":
    solve()
