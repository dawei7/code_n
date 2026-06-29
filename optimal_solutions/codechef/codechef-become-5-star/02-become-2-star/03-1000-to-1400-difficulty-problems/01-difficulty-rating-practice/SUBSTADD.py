# cook your dish here


def solve():
    T = int(input())

    for tc in range (T):
        N,X,Y = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        V = 'Yes'
        for i in range (N):
            if ((B[i]-A[i] != X) and (B[i]-A[i] != Y)):
                V = 'No'
                break
        print(V)


if __name__ == "__main__":
    solve()
