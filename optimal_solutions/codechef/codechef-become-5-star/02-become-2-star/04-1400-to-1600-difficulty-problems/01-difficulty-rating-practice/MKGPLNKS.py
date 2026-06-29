import math


def solve():
    T = int(input())
    for _ in range(T):
        N = int(input());
        S = input();

        chunk = 0
        for i in range(N-1):
            if(S[i] != S[i+1]):
                chunk += 1;
        print(math.ceil(chunk / 2))


if __name__ == "__main__":
    solve()
