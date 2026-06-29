# cook your dish here


def solve():
    for _ in range(int(input())):
        s1=input()
        s2=input()
        m1=0
        m2=0
        for i in range(len(s1)):
            if(s1[i]!='?' and s2[i]!='?' and s1[i]!=s2[i]):
                m1+=1 
            elif(s1[i]=='?' or s2[i]=='?'):
                m2+=1 
        print(m1,'',m1+m2)


if __name__ == "__main__":
    solve()
