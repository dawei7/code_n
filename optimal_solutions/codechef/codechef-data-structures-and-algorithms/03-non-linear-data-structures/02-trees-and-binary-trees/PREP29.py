import sys
sys.setrecursionlimit(300000)
MOD = 10 ** 9 + 7

def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    index = 1
    res = []
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        values = [0] + list(map(int, input_data[index:index + n]))
        index += n
        tree = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = int(input_data[index])
            v = int(input_data[index + 1])
            index += 2
            tree[u].append(v)
        total = 0

        def dfs(node, curr):
            nonlocal total
            curr = (curr * 10 + values[node]) % MOD
            if not tree[node]:
                total = (total + curr) % MOD
                return
            for child in tree[node]:
                dfs(child, curr)
        dfs(1, 0)
        res.append(str(total))
    sys.stdout.write('\n'.join(res))


if __name__ == "__main__":
    solve()
