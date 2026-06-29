


def solve():
    for _ in range(int(input())):
        n,k=[int(x) for x in input().split()]
        s=[int(x) for x in input().split()]
        if max(s)-n<k:
            print(n+k)
        else:
            temp=[0]*(max(s)+1)
            for i in s:
                temp[i]=1
            for i in range(len(temp)):
                if temp[i]==0:
                    if k==0:
                        print(i)
                        break
                    k-=1


if __name__ == "__main__":
    solve()
