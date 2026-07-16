"""Optimal app-local solution for LeetCode 1519."""


def solve(n, edges, labels):
    graph = [[] for _ in range(n)]
    for first, second in edges:
        graph[first].append(second)
        graph[second].append(first)

    seen = [0] * 26
    before = [0] * n
    answer = [0] * n
    stack = [(0, -1, False)]
    while stack:
        node, parent, exiting = stack.pop()
        label = ord(labels[node]) - ord("a")
        if exiting:
            answer[node] = seen[label] - before[node]
        else:
            before[node] = seen[label]
            seen[label] += 1
            stack.append((node, parent, True))
            for neighbor in graph[node]:
                if neighbor != parent:
                    stack.append((neighbor, node, False))
    return answer
