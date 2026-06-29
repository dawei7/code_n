


def solve():
    T = int(input())

    for t in range(T):
        N, K = map(int, input().split())

        nodd = N // 2 
        if N % 2 == 1: 
            nodd += 1 

        if nodd < K or K > N//2 or (nodd % 2 != K % 2):
            print("NO")
        else:
            print("YES")


if __name__ == "__main__":
    solve()
