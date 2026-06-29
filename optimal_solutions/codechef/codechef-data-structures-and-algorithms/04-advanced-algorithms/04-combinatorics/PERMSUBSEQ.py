MOD = 1000000007

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        freq = [0] * (n + 1)
        for i in range(n):
            a = int(data[index])
            index += 1
            if a <= n:
                freq[a] += 1
        sum = 0
        prefix = 1
        for i in range(1, n + 1):
            prefix = prefix * freq[i] % MOD
            sum = (sum + prefix) % MOD
        results.append(sum)
    for result in results:
        print(result)


if __name__ == "__main__":
    solve()
