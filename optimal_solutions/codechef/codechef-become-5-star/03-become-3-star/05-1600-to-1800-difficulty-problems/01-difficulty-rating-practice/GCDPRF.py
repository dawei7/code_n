# cook your dish here


def solve():
    def func(arr):
        for i in range(0,len(arr)-1):
            if arr[i]%arr[i+1]!=0:
                return -1
        res = ' '.join([str(s) for s in arr])
        return res
    t=int(input())
    for i in range(0,t):
        n=int(input())
        arr=list(map(int,input().split()))
        print(func(arr))


if __name__ == "__main__":
    solve()
