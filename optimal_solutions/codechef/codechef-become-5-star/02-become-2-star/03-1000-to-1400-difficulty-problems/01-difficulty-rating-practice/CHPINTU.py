# cook your dish here


def solve():
    n=int(input())
    for i in range(n):
        a,b=map(int,input().split())
        f=list(map(int,input().split()))
        v=list(map(int,input().split()))
        freq={}
        j=0
        for i in f:
            if i in freq:
                freq[i]=freq[i]+v[j]
            else:
                freq[i]=v[j]
            j=j+1
        mini=min(freq.values())
        print(mini)


if __name__ == "__main__":
    solve()
