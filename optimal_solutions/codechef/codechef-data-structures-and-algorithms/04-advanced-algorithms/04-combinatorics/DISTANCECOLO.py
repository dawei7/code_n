MOD = 1000000007

def compute_result(n, k):
    if n > k:
        ans = 1
        for i in range(1, k + 1):
            ans = ans * i % MOD
    else:
        ans = 1
        for i in range(k - n + 1, k + 1):
            ans = ans * i % MOD
    return ans

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
        k = int(data[index + 1])
        index += 2
        result = compute_result(n, k)
        results.append(result)
    for result in results:
        print(result)


if __name__ == "__main__":
    solve()
