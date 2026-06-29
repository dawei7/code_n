from collections import deque, defaultdict

def solve():
    n = int(input())
    tree = defaultdict(list)
    for _ in range(1, n):
        u, v = map(int, input().split())
        tree[u].append(v)
    q = deque()
    vis = set()
    q.append(1)
    while q:
        u = q.popleft()
        print(u, end=' ')
        vis.add(u)
        for v in tree[u]:
            if v not in vis:
                q.append(v)


if __name__ == "__main__":
    solve()
