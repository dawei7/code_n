from collections import deque, defaultdict

def find_order(n, adj, indegree):
    q = deque()
    course_order = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        node = q.popleft()
        course_order.append(node)
        for v in adj[node]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    if len(course_order) == n:
        print(' '.join(map(str, course_order)))
    else:
        print(-1)

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    index = 0
    n = int(data[index])
    index += 1
    m = int(data[index])
    index += 1
    adj = defaultdict(list)
    indegree = [0] * (n + 1)
    for _ in range(m):
        a = int(data[index])
        index += 1
        b = int(data[index])
        index += 1
        adj[a].append(b)
        indegree[b] += 1
    find_order(n, adj, indegree)


if __name__ == "__main__":
    solve()
