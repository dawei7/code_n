# cook your dish here


def solve():
    for T in range(int(input())):

        N,K = map(int,input().split())

        if N == 1:
            print(1)

        elif K > N//2:
            print(-1)

        else:
            for i in range(2,2*K+2,2):
                print(i, end=" ")
            print()


if __name__ == "__main__":
    solve()
