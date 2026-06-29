


def solve():
    for _ in range(int(input())):
        N = int(input())
        P = [int(x) for x in input().split()]
        Q = [int(x) for x in input().split()]
        sum=0
        oddP=0
        oddQ =0
        for i in range(N):
            if P[i]%2:
                oddP += 1
            if Q[i]%2:
                oddQ += 1
            sum += (P[i]+Q[i])/2
        print(int(sum-0.5*(oddP-oddQ if oddP > oddQ else oddQ-oddP)))


if __name__ == "__main__":
    solve()
