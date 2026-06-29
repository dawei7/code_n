# cook your dish here


def solve():
    T=int(input())
    for i in range(T):
        A=list(map(int,input().split()))
        #A[0]=A,A[1]=B,A[2]=C
        A.sort()
        print(A[-1]+A[-2])


if __name__ == "__main__":
    solve()
