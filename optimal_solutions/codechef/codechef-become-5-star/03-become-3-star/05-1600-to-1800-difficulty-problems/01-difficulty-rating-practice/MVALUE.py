


def solve():
    t=int(input())
    for i in range(t):
        n=int(input())
        A=list(map(int,input().split()))
        A.sort()
        left=(A[1]-1)*(A[0]+1)
        left+=1 
        right=(A[-1]-1)*(A[-2]+1)
        right+=1 
        print(max(left,right))


if __name__ == "__main__":
    solve()
