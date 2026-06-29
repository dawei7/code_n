


def solve():
    T = int(input())

    for _ in range(T):
        N = int(input())
        L = list(map(int,input().split()))

        p = 0
        for i in range(len(L)-1):
            c = L[i] & L[i+1]
            print(max(c,p), end = ' ')
            p = c
        print(c)


if __name__ == "__main__":
    solve()
