


def solve():
    def inverse(num):
        mod =10**9+7
        a = mod-2
        result = 1
        result=pow(num,a,mod)
        return result

    def calculate_probability(n,l,fact):
        d={}
        for n1,n2 in l:
            if n1 in d:
                d[n1]+=1 
            else:
                d[n1]=1

        mod=10**9+7
        nume=1
        for i in d:
            nume=(nume*fact[d[i]])%mod

        deno=fact[-1]
        inv=inverse(deno)

        probability=(nume*inv)%mod
        return probability



    n=int(input())
    mod=10**9+7
    fact=[0 for i in range(n+1)]
    fact[0]=1
    for i in range(1,n+1):
        fact[i]=(i*fact[i-1])%mod
    l=[]
    for i in range(n):
        t=list(map(int,input().split()))
        l.append(t)


    ans=calculate_probability(n,l,fact)
    print(ans)


if __name__ == "__main__":
    solve()
