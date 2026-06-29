import sys
input = sys.stdin.read

def solve():
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        S = data[index + 2]
        index += 3
        Pre = [0] * (N + 1)
        for i in range(N):
            Pre[i + 1] = Pre[i] + (1 if S[i] == '1' else 0)
        one_count = 0
        for i in range(K):
            ones_in_range = Pre[N - K + i + 1] - Pre[i]
            if ones_in_range % 2 == 1:
                one_count += 1
        results.append(str(one_count))
    print('\n'.join(results))


if __name__ == "__main__":
    solve()
