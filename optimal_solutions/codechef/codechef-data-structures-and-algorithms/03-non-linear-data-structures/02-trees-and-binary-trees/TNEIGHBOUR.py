import sys
input = sys.stdin.read

def solve():
    data = input().strip().split()
    n = int(data[0])
    v = int(data[1])
    degree = [0] * (n + 1)
    assert 1 <= v <= n
    index = 2
    for _ in range(n - 1):
        x = int(data[index])
        y = int(data[index + 1])
        degree[x] += 1
        degree[y] += 1
        index += 2
    print(degree[v])


if __name__ == "__main__":
    solve()
