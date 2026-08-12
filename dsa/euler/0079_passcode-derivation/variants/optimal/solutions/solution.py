from collections import defaultdict, deque
import urllib.request


def solve() -> int:
    """Determine the shortest secret passcode from keylog.txt using Topological Sort.
    
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    """
    url = "https://projecteuler.net/resources/documents/0079_keylog.txt"
    with urllib.request.urlopen(url, timeout=5) as resp:
        text = resp.read().decode("utf-8")

    attempts = [line.strip() for line in text.strip().splitlines() if line.strip()]

    graph = defaultdict(set)
    in_degree = defaultdict(int)
    nodes = set()

    for attempt in attempts:
        c1, c2, c3 = attempt[0], attempt[1], attempt[2]
        nodes.update([c1, c2, c3])
        if c2 not in graph[c1]:
            graph[c1].add(c2)
            in_degree[c2] += 1
        if c3 not in graph[c2]:
            graph[c2].add(c3)
            in_degree[c3] += 1

    queue = deque([n for n in nodes if in_degree[n] == 0])
    passcode = []

    while queue:
        node = queue.popleft()
        passcode.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return int("".join(passcode))
