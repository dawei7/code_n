


def solve():
    t = int(input())
    for _ in range(t):
        N = int(input())
        C = [0] + list(map(int, input().split()))
        W = [0] + list(map(int, input().split()))
        seen = [0 for _ in range(N + 1)]

        result = 0
        current_sum = 0
        L = 1
        R = 1

        for i in range(1, N + 1):
            seen[i] = False  # Initialize all elements as unseen

        while True:
            while R <= N and not seen[C[R]]:
                current_sum += W[R]
                seen[C[R]] = True
                R += 1
            result = max(result, current_sum)
            if R == N + 1:
                break
            while seen[C[R]]:
                seen[C[L]] = False
                current_sum -= W[L]
                L += 1
        print(result)


if __name__ == "__main__":
    solve()
