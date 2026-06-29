# cook your dish here


def solve():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int,input().split()))
        result_min = [0]*n 
        result_max = [0]*n
        for i in range(n):
            mex = a[i]
            result_min[0] += 1 
            if mex < n :
                result_min[mex] -= 1

            result_max[0] += n - (mex - 1)    
            if mex < n:
                result_max[mex] -= n - (mex - 1)

            if mex < n-1:
                result_max[mex + 1] += n - mex

        pre_min = result_min[0]
        pre_max = result_max[0]
        print(pre_min, pre_max)
        for i in range(1,n):
            pre_min += result_min[i]
            pre_max += result_max[i]

            print(pre_min, pre_max)


if __name__ == "__main__":
    solve()
