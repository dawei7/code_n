# cook your dish here


def solve():
    t  = int(input())
    arr = []

    for i in range(0,31):
        for j in range(i+1,31):
            arr.append((1<<i)+(1<<j))
    arr.sort()

    for test in range(t):
        n = int(input())


        l = 0 
        r = len(arr)
        lowerbound = float("-inf")
        while(l<=r):
            m = l+(r-l)//2
            if arr[m]==n:
                lowerbound = -1
                break
            elif arr[m]>n:
                r = m-1
            else:
                l = m+1 
        if lowerbound==-1:
            print(0)
            continue
        lowerbound = arr[r]
        upbound = arr[l]
        print(min(abs(upbound-n),abs(n-lowerbound)))


if __name__ == "__main__":
    solve()
