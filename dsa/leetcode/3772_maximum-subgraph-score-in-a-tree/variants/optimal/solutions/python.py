def solve(n: int, edges: list[list[int]], good: list[int]) -> list[int]:
    neighbors = [[] for _ in range(n)]
    for left, right in edges:
        neighbors[left].append(right)
        neighbors[right].append(left)

    parents = [-1] * n
    traversal = [0]
    for node in traversal:
        for adjacent in neighbors[node]:
            if adjacent != parents[node]:
                parents[adjacent] = node
                traversal.append(adjacent)

    subtree_score = [2 * value - 1 for value in good]
    for node in traversal[:0:-1]:
        if subtree_score[node] > 0:
            subtree_score[parents[node]] += subtree_score[node]

    maximum = subtree_score.copy()
    for node in traversal[1:]:
        parent = parents[node]
        outside = maximum[parent] - max(0, subtree_score[node])
        maximum[node] += max(0, outside)

    return maximum
