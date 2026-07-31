def solve(edges: list[list[int]], guesses: list[list[int]], k: int) -> int:
    node_count = len(edges) + 1
    graph = [[] for _ in range(node_count)]
    for first, second in edges:
        graph[first].append(second)
        graph[second].append(first)

    guess_set = {tuple(guess) for guess in guesses}
    parent = [-2] * node_count
    parent[0] = -1
    order = [0]

    for node in order:
        for neighbor in graph[node]:
            if neighbor != parent[node]:
                parent[neighbor] = node
                order.append(neighbor)

    correct = [0] * node_count
    correct[0] = sum((parent[node], node) in guess_set for node in range(1, node_count))
    answer = int(correct[0] >= k)

    for node in order[1:]:
        previous_root = parent[node]
        correct[node] = (
            correct[previous_root] - ((previous_root, node) in guess_set) + ((node, previous_root) in guess_set)
        )
        answer += correct[node] >= k

    return answer
