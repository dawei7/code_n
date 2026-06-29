import sys
import collections
sys.setrecursionlimit(300000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        children = collections.defaultdict(list)
        parent = {}
        root = None
        nodes = set()
        for i in range(n):
            par = int(data[index])
            node = int(data[index + 1])
            index += 2
            nodes.add(node)
            if par == -1:
                root = node
            else:
                parent[node] = par
                children[par].append(node)
        depth = {}
        queue = collections.deque()
        depth[root] = 0
        queue.append(root)
        while queue:
            cur = queue.popleft()
            for child in children[cur]:
                depth[child] = depth[cur] + 1
                queue.append(child)
        a = int(data[index])
        b = int(data[index + 1])
        c = int(data[index + 2])
        index += 3

        def lca(u, v):
            while depth[u] > depth[v]:
                u = parent[u]
            while depth[v] > depth[u]:
                v = parent[v]
            while u != v:
                u = parent[u]
                v = parent[v]
            return u
        res = lca(lca(a, b), c)
        results.append(str(res))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
