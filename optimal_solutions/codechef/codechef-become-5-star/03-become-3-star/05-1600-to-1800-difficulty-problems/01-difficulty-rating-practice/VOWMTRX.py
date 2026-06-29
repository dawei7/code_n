import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    T = int(input_data[0])
    idx = 1
    MOD = 10 ** 9 + 7
    out = []
    for _ in range(T):
        N = int(input_data[idx])
        K = int(input_data[idx + 1])
        S = input_data[idx + 2]
        idx += 3
        vowels = []
        for i in range(N):
            if S[i] in 'aeiou':
                vowels.append(i)
        ans = 1
        for i in range(K, len(vowels), K):
            ans = ans * (vowels[i] - vowels[i - 1]) % MOD
        out.append(str(ans))
    print('\n'.join(out))


if __name__ == "__main__":
    solve()
