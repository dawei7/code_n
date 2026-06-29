def solve():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = [0] * (n + 1)
        x = list(map(int, data[index].split()))
        for num in x:
            if 1 <= num <= n:
                a[num] += 1
        index += 1
        sum_ratings = 0
        ans = 0
        for i in range(1, n + 1):
            sum_ratings += a[i]
            ans = max(ans, (sum_ratings + i - 1) // i)
        results.append(ans)
    print('\n'.join(map(str, results)))


if __name__ == "__main__":
    solve()
